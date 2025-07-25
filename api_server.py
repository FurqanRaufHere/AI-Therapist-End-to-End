# api_server.py
# from fastapi import FastAPI, HTTPException, Request
# from pydantic import BaseModel
# from rag_query_system import generate_response
# from fastapi.middleware.cors import CORSMiddleware
# import logging
# import os

# app = FastAPI()

# # Configure logging
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger("api_server")

# # Allow CORS for frontend development
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # Adjust this in production
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # Mock user database
# users_db = {}

# class QueryRequest(BaseModel):
#     query: str

# class QueryResponse(BaseModel):
#     answer: str

# class UserAuthRequest(BaseModel):
#     email: str
#     password: str
#     name: str = None  # Optional for login

# class UserAuthResponse(BaseModel):
#     name: str
#     email: str


# # 🧠 Replace the /api/chat function with this:
# @app.post("/api/chat", response_model=QueryResponse)
# async def chat_endpoint(request: Request, body: QueryRequest):
#     logger.info(f"Received /api/chat request with query: {body.query}")
#     try:
#         answer, _ = generate_response(body.query)
#         logger.info("Generated response successfully")
#         return QueryResponse(answer=answer)
#     except Exception as e:
#         import traceback
#         logger.error("Detailed error:\n" + traceback.format_exc())
#         raise HTTPException(status_code=500, detail="Internal Server Error — see backend logs.")

# @app.post("/api/register", response_model=UserAuthResponse)
# async def register_user(request: UserAuthRequest):
#     if not request.name:
#         raise HTTPException(status_code=400, detail="Name is required for registration")
#     if request.email in users_db:
#         raise HTTPException(status_code=400, detail="User already exists")
#     # Simple user creation
#     users_db[request.email] = {"name": request.name, "password": request.password}
#     return UserAuthResponse(name=request.name, email=request.email)

# @app.post("/api/login", response_model=UserAuthResponse)
# async def login_user(request: UserAuthRequest):
#     user = users_db.get(request.email)
#     if not user or user["password"] != request.password:
#         raise HTTPException(status_code=401, detail="Invalid email or password")
#     return UserAuthResponse(name=user["name"], email=request.email)

# # ✅ Add this at the bottom of the file:
# @app.get("/")
# async def health_check():
#     return {"status": "AI Therapist backend is running"}

# if __name__ == "__main__":
#     import uvicorn
#     port = int(os.environ.get("PORT", 8000))
#     uvicorn.run("api_server:app", host="0.0.0.0", port=port, reload=True)




from fastapi import FastAPI, HTTPException, Request, Depends, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
from rag_query_system import generate_response
from fastapi.middleware.cors import CORSMiddleware
import logging
import os
import json
import jwt
import hashlib
from datetime import datetime, timedelta
from typing import Optional

app = FastAPI()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("api_server")

# JWT Configuration
SECRET_KEY = os.getenv("JWT_SECRET_KEY", "your-secret-key-change-this-in-production")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 1440  # 24 hours

# Security
security = HTTPBearer()

# Allow CORS for frontend development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# File-based user storage
USERS_FILE = "users_database.json"

def load_users():
    """Load users from JSON file"""
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_users(users_data):
    """Save users to JSON file"""
    with open(USERS_FILE, 'w') as f:
        json.dump(users_data, f, indent=2)

def hash_password(password: str) -> str:
    """Hash password using SHA256"""
    return hashlib.sha256(password.encode()).hexdigest()

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify password against hash"""
    return hash_password(plain_password) == hashed_password

def create_access_token(data: dict):
    """Create JWT access token"""
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    """Verify JWT token"""
    try:
        payload = jwt.decode(credentials.credentials, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        return email
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

# Request/Response Models
class QueryRequest(BaseModel):
    query: str

class QueryResponse(BaseModel):
    answer: str

class UserRegisterRequest(BaseModel):
    email: str
    password: str
    name: str

class UserLoginRequest(BaseModel):
    email: str
    password: str

class UserAuthResponse(BaseModel):
    name: str
    email: str
    access_token: str
    token_type: str = "bearer"

class UserProfileResponse(BaseModel):
    name: str
    email: str
    created_at: str
    last_login: str

@app.post("/api/register", response_model=UserAuthResponse)
async def register_user(request: UserRegisterRequest):
    users_db = load_users()
    
    if request.email in users_db:
        raise HTTPException(status_code=400, detail="User already exists")
    
    # Create new user
    hashed_password = hash_password(request.password)
    user_data = {
        "name": request.name,
        "email": request.email,
        "password": hashed_password,
        "created_at": datetime.utcnow().isoformat(),
        "last_login": datetime.utcnow().isoformat()
    }
    
    users_db[request.email] = user_data
    save_users(users_db)
    
    # Create access token
    access_token = create_access_token(data={"sub": request.email})
    
    return UserAuthResponse(
        name=request.name,
        email=request.email,
        access_token=access_token
    )

@app.post("/api/login", response_model=UserAuthResponse)
async def login_user(request: UserLoginRequest):
    users_db = load_users()
    user = users_db.get(request.email)
    
    if not user or not verify_password(request.password, user["password"]):
        raise HTTPException(status_code=401, detail="Invalid email or password")
    
    # Update last login
    user["last_login"] = datetime.utcnow().isoformat()
    users_db[request.email] = user
    save_users(users_db)
    
    # Create access token
    access_token = create_access_token(data={"sub": request.email})
    
    return UserAuthResponse(
        name=user["name"],
        email=request.email,
        access_token=access_token
    )

@app.get("/api/profile", response_model=UserProfileResponse)
async def get_user_profile(current_user_email: str = Depends(verify_token)):
    users_db = load_users()
    user = users_db.get(current_user_email)
    
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    return UserProfileResponse(
        name=user["name"],
        email=user["email"],
        created_at=user["created_at"],
        last_login=user["last_login"]
    )

@app.post("/api/chat", response_model=QueryResponse)
async def chat_endpoint(
    request: Request, 
    body: QueryRequest,
    current_user_email: str = Depends(verify_token)
):
    logger.info(f"User {current_user_email} sent query: {body.query}")
    try:
        answer, _ = generate_response(body.query)
        logger.info("Generated response successfully")
        return QueryResponse(answer=answer)
    except Exception as e:
        logger.error(f"Error in /api/chat: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/logout")
async def logout_user(current_user_email: str = Depends(verify_token)):
    # In a real application, you might want to blacklist the token
    # For now, we'll just return a success message
    return {"message": "Successfully logged out"}

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("api_server:app", host="0.0.0.0", port=port, reload=True)