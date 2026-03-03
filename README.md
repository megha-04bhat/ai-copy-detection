# ai-copy-detection
# 📘 AI Copy Detection Service

An AI-powered document similarity and ownership verification module built using:

- FastAPI
- PostgreSQL
- FAISS
- Sentence Transformers
- OCR (Tesseract)
- Invisible Watermarking

This module is part of the **Academic & Career Assistance Platform** and is responsible for detecting:

1. Exact copied questions (via invisible watermark)
2. Modified copies (via semantic similarity)
3. New questions

---

## 🚀 Features

- ✅ Invisible watermark embedding  
- ✅ Watermark detection during upload  
- ✅ OCR support for scanned PDFs  
- ✅ Semantic similarity using Sentence Transformers  
- ✅ FAISS-based vector search  
- ✅ PostgreSQL-backed question storage  
- ✅ Clean modular architecture  
- ✅ Production-ready structure  

---

## 🏗 Project Structure
    copy-detection/
    ├─ app/
    │ ├─ database/
    │ ├─ services/
    │ ├─ similarity/
    │ ├─ utils/
    │ └─ watermark/
    ├─ data/
    ├─ tests/
    ├─ .env
    ├─ requirements.txt
    └─ README.md
---

### 📌 Document Upload Flow


User uploads document
↓
Text extraction (PDF/DOCX/OCR)
↓
Watermark detection
→ If found → EXACT_COPY
↓
FAISS similarity search
↓
Threshold classification
↓
Return result


---

## 🧾 Classification Logic

| Condition | Result |
|-----------|--------|
| Watermark found | EXACT_COPY |
| Similarity ≥ 0.85 | HIGH_CONFIDENCE_COPY |
| Similarity ≥ 0.65 | MODIFIED_COPY |
| Otherwise | NEW_QUESTION |

---

<h2>🛠️ Installation Steps:</h2>

<p>1️⃣ Clone Repository</p>

```
git clone  cd copy-detection
```
<p> 2️⃣ Create Virtual Environment</p>
<p>Windows</p>

```
python -m venv venv 
venv\Scripts\activate
```
<p>Mac / Linux</p>

```
python3 -m venv venv
source venv/bin/activate
```
<p>3️⃣ Install Dependencies</p>

```
pip install -r requirements.txt
```

<p>4️⃣ Configure Environment Variables</p>

Create a .env file in the project root:

```
DB_NAME=copy_detection
DB_USER=postgres
DB_PASSWORD=yourpassword
DB_HOST=localhost
DB_PORT=5432
```

<p>5️⃣ Setup PostgreSQL</p>

Create the table:

```
CREATE TABLE questions (
    question_id SERIAL PRIMARY KEY,
    question_text TEXT NOT NULL
);
```

Insert sample data:
```
INSERT INTO questions (question_text) VALUES
('Explain Newton''s First Law of Motion in detail.'),
('Define Ohm''s Law.'),
('What is Artificial Intelligence?');
```
<p>6️⃣ Install Tesseract (For OCR Support)</p>

Download Windows installer from:

https://github.com/UB-Mannheim/tesseract/wiki

After installation, update the path inside:

```
app/utils/text_extractor.py
```

Example:
```
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
```

<p>▶️ Run Application</p>

```
uvicorn app.main:app --reload
```
Open Swagger UI:

http://127.0.0.1:8000/docs

Use the /check-copy endpoint.

📦 API Endpoint
POST /check-copy

Upload a PDF or DOCX file.
```
Example Response
{
  "status": "MODIFIED_COPY",
  "similarity_score": 0.87,
  "matched_question_id": 3,
  "matched_question": "Explain Newton's First Law..."
}
```
