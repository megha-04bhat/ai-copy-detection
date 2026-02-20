import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

# =========================
# MODEL CONFIG
# =========================
MODEL_NAME = os.getenv("MODEL_NAME", "all-mpnet-base-v2")

# =========================
# SIMILARITY THRESHOLDS
# =========================
SIMILARITY_THRESHOLD = float(os.getenv("SIMILARITY_THRESHOLD", 0.70))
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