from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from rag_query_system import generate_response
from fastapi.middleware.cors import CORSMiddleware
import logging

app = FastAPI()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("api_server")

# Allow CORS for frontend development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mock user database
users_db = {}

class QueryRequest(BaseModel):
    query: str

class QueryResponse(BaseModel):
    answer: str

class UserAuthRequest(BaseModel):
    email: str
    password: str
    name: str = None  # Optional for login

class UserAuthResponse(BaseModel):
    name: str
    email: str

@app.post("/api/chat", response_model=QueryResponse)
async def chat_endpoint(request: Request, body: QueryRequest):
    logger.info(f"Received /api/chat request with query: {body.query}")
    try:
        answer, _ = generate_response(body.query)
        logger.info("Generated response successfully")
        return QueryResponse(answer=answer)
    except Exception as e:
        logger.error(f"Error in /api/chat: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/register", response_model=UserAuthResponse)
async def register_user(request: UserAuthRequest):
    if not request.name:
        raise HTTPException(status_code=400, detail="Name is required for registration")
    if request.email in users_db:
        raise HTTPException(status_code=400, detail="User already exists")
    # Simple user creation
    users_db[request.email] = {"name": request.name, "password": request.password}
    return UserAuthResponse(name=request.name, email=request.email)

@app.post("/api/login", response_model=UserAuthResponse)
async def login_user(request: UserAuthRequest):
    user = users_db.get(request.email)
    if not user or user["password"] != request.password:
        raise HTTPException(status_code=401, detail="Invalid email or password")
    return UserAuthResponse(name=user["name"], email=request.email)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
