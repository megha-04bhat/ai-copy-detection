import re

WATERMARK_PATTERN = r"QID:TS-Q-\d{4}-\d{3}-[A-Z0-9]+"

def detect_watermark(extracted_text):
    match = re.search(WATERMARK_PATTERN, extracted_text)
    if match:
        watermark = match.group()
        cleaned_text = re.sub(WATERMARK_PATTERN, "", extracted_text).strip()

        return True, watermark, cleaned_text

    return False, None, extracted_text
    
    