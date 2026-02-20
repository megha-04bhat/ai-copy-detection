import pdfplumber
import pytesseract
import io
from pdf2image import convert_from_bytes
from docx import Document
from app.config import TESSERACT_PATH, POPPLER_PATH

if TESSERACT_PATH:
    pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH



def extract_pdf_text(file_bytes: bytes) -> str:
    """
    Extracts text from a PDF file (non-scanned).
    """
    text = ""
    with pdfplumber.open(io.BytesIO(file_bytes)) as pdf:
        for page in pdf.pages:
            extracted = page.extract_text()
            if extracted:
                text += extracted + "\n"
    if len(text.strip()) < 20:
        text = extract_pdf_ocr(file_bytes)
    return text

def extract_pdf_ocr(file_bytes: bytes) -> str:
    """
    OCR extraction for scanned PDFs.
    """
    text = ""
    images = convert_from_bytes(file_bytes, poppler_path=POPPLER_PATH)

    for image in images:
        ocr_result = pytesseract.image_to_string(image)
        text += ocr_result + "\n"
    return text

def extract_docx_text(file_bytes: bytes) -> str:
    """
    Extracts text from a DOCX file.
    """
    document = Document(io.BytesIO(file_bytes))
    text = "\n".join([para.text for para in document.paragraphs])
    return text


def extract_text(file_bytes: bytes, filename: str) -> str:
    """
    Detects file type and routes to correct extractor.
    """

    if filename.lower().endswith(".pdf"):
        return extract_pdf_text(file_bytes)

    elif filename.lower().endswith(".docx"):
        return extract_docx_text(file_bytes)

    else:
        raise ValueError("Unsupported file format. Only PDF and DOCX are supported.")
