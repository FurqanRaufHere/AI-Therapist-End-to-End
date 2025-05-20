# # extract_pdf.py

# import os
# import json
# from PyPDF2 import PdfReader

# DATA_DIR = "./Data"
# OUTPUT_FILE = "./ProcessedData/extracted_texts.json"
# os.makedirs("ProcessedData", exist_ok=True)

# def extract_text_from_pdfs():
#     extracted = []
#     for filename in os.listdir(DATA_DIR):
#         if filename.endswith(".pdf"):
#             path = os.path.join(DATA_DIR, filename)
#             reader = PdfReader(path)
#             full_text = ""
#             for page in reader.pages:
#                 content = page.extract_text()
#                 if content:
#                     full_text += content.strip() + "\n"
#             extracted.append({
#                 "file": filename,
#                 "content": full_text
#             })
#     return extracted

# if __name__ == "__main__":
#     results = extract_text_from_pdfs()
#     with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
#         json.dump(results, f, indent=4, ensure_ascii=False)
#     print(f"[✓] Extracted text saved to {OUTPUT_FILE}")


# extract_pdf.py

import os
import json
from PyPDF2 import PdfReader

DATA_DIR = "./Data"
OUTPUT_FILE = "./ProcessedData/extracted_texts.json"
THERAPY_JSON = os.path.join(DATA_DIR, "TherapyData.json")

os.makedirs("ProcessedData", exist_ok=True)

def extract_text_from_pdfs():
    pdf_data = []
    for filename in os.listdir(DATA_DIR):
        if filename.lower().endswith(".pdf"):
            path = os.path.join(DATA_DIR, filename)
            reader = PdfReader(path)
            text = ""
            for page in reader.pages:
                content = page.extract_text()
                if content:
                    text += content.strip() + "\n"
            pdf_data.append({
                "source": filename,
                "content": text.strip()
            })
    return pdf_data

def extract_text_from_json():
    json_data = []
    if not os.path.exists(THERAPY_JSON):
        print(f"[!] JSON file not found: {THERAPY_JSON}")
        return json_data
    
    with open(THERAPY_JSON, "r", encoding="utf-8") as f:
        try:
            items = json.load(f)
            for item in items:
                question = item.get("question", "").strip()
                answer = item.get("answer", "").strip()
                if question and answer:
                    combined = f"Q: {question}\nA: {answer}"
                    json_data.append({
                        "source": "TherapyData.json",
                        "content": combined
                    })
        except Exception as e:
            print(f"[!] Error parsing TherapyData.json: {e}")
    return json_data

if __name__ == "__main__":
    all_data = extract_text_from_pdfs() + extract_text_from_json()
    
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(all_data, f, indent=4, ensure_ascii=False)

    print(f"[✓] Extracted text from PDFs + JSON saved to {OUTPUT_FILE}")
