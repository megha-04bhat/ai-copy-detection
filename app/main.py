# @app.post("/extract")
# async def extract(file: UploadFile = File(...)):
#     file_bytes = await file.read()
#     text = extract_text(file_bytes, file.filename)
#     return {"extracted_text": text}


# @app.post("/check_watermark")
# async def check_watermark(file: UploadFile = File(...)):

#     file_bytes = await file.read()
#     extracted_text = extract_text(file_bytes, file.filename)



#     found, watermark = detect_watermark(extracted_text)

#     if found:
#         return{
#             "status": "EXACT_COPY",
#             "watermark": watermark
#         }
#     return{
#         "status": "NO_WATERMARK"
#     }


# pyrefly: ignore [missing-import]
from fastapi import FastAPI, UploadFile, File
from contextlib import asynccontextmanager
# pyrefly: ignore [missing-import]
from fastapi.middleware.cors import CORSMiddleware

from app.utils.text_extractor import extract_text
from app.utils.pdf_to_json import convert_text_to_json
from app.services.decision_engine import evaluate_document
from app.watermark.detect import detect_watermark
import app.similarity.faiss_index as faiss_store
from app.database.questions import get_all_questions
from app.similarity.faiss_index import add_question

origins = [
    "http://localhost:5173",
    "http://localhost:3000",
    "http://localhost:8000"
]



# ---------------------------------------------------
# SAMPLE QUESTIONS (Only added if index empty)
# ---------------------------------------------------
# DATABASE_QUESTIONS = [
#     "Explain Newton's First Law of Motion in detail.",
#     "Define Ohm's Law.",
#     "What is Artificial Intelligence?"
# ]

# ---------------------------------------------------
# LIFESPAN HANDLER (Modern FastAPI)
# ---------------------------------------------------
@asynccontextmanager
async def lifespan(app: FastAPI):
    # print("Initializing FAISS index...")
    # faiss_store.initialize_index()

    # print("Index total after init:", faiss_store.index.ntotal)

    # if faiss_store.index.ntotal == 0:
    #     print("Adding sample questions...")
    #     for question in DATABASE_QUESTIONS:
    #         faiss_store.add_question(question)

    # print("System ready.")
    # yield
    # print("Shutting down AI Copy Detection Service...")

    print("Loading questions from PostgreSQL...")

    rows = get_all_questions()

    for question_id, question_text in rows:
        add_question(question_id, question_text)

    print("FAISS index loaded successfully.")

    yield


# ---------------------------------------------------
# CREATE FASTAPI APP
# ---------------------------------------------------
app = FastAPI(lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ---------------------------------------------------
# HEALTH CHECK
# ---------------------------------------------------
@app.get("/")
def home():
    return {"message": "AI Copy Detection Service Running"}


# ---------------------------------------------------
# PDF → JSON Endpoint
# ---------------------------------------------------
@app.post("/pdf-to-json")
async def pdf_to_json(file: UploadFile = File(...)):
    file_bytes = await file.read()
    extracted_text = extract_text(file_bytes, file.filename)

    # Remove watermark before converting
    _, _, cleaned_text = detect_watermark(extracted_text)

    structured_json = convert_text_to_json(cleaned_text)
    return structured_json


# ---------------------------------------------------
# MAIN COPY DETECTION (Per Question)
# ---------------------------------------------------
@app.post("/check-copy")
async def check_copy(file: UploadFile = File(...)):
    file_bytes = await file.read()

    # Step 1: Extract raw text
    extracted_text = extract_text(file_bytes, file.filename)

    # Step 2: Detect and remove watermark
    has_watermark, watermark, cleaned_text = detect_watermark(extracted_text)

    # 🔥 If watermark exists → immediate EXACT_COPY
    if has_watermark:
        return {
            # "total_questions": 1,
            "results": [
                {
                    # "question_number": 1,
                    "analysis": {
                        "status": "EXACT_COPY",
                        "watermark": watermark
                    }
                }
            ]
        }


    # Step 3: Convert to structured JSON
    structured = convert_text_to_json(cleaned_text)

    results = []

    # Step 4: Evaluate each question separately
    for question in structured["questions"]:
        analysis = evaluate_document(question["question_text"])

        results.append({
            "question_number": question["question_number"],
            "analysis": analysis
        })

    return {
        "total_questions": len(results),
        "results": results
    }








