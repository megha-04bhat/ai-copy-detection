import re

WATERMARK_PATTERN = r"QID:TS-Q-\d{4}-\d{3}-[A-Z0-9]+"

def detect_watermark(extracted_text):
    match = re.search(WATERMARK_PATTERN, extracted_text)
    if match:
        return True, match.group()
    return False, None