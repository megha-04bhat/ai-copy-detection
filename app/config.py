import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

DB_CONFIG = {
    "dbname": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "host": os.getenv("DB_HOST"),
    "port": os.getenv("DB_PORT")
}

# =========================
# MODEL CONFIG
# =========================
MODEL_NAME = os.getenv("MODEL_NAME", "all-mpnet-base-v2")

# =========================
# SIMILARITY THRESHOLDS
# =========================
SIMILARITY_THRESHOLD = float(os.getenv("SIMILARITY_THRESHOLD", 0.65))
HIGH_CONFIDENCE_THRESHOLD = float(os.getenv("HIGH_CONFIDENCE_THRESHOLD", 0.85))

# =========================
# DEBUG MODE
# =========================
DEBUG = os.getenv("DEBUG", "True") == "True"

# =========================
# OCR CONFIG
# =========================
TESSERACT_PATH = os.getenv("TESSERACT_PATH")
POPPLER_PATH = os.getenv("POPPLER_PATH")