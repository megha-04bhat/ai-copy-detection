# import os
# import uuid
# import sys
# from app.watermark.embed import watermark_existing_pdf

# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# INPUT_FOLDER = "documents"
# OUTPUT_FOLDER = "watermarked"

# os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# question_id = "TS-Q-2026-001"

# for file in os.listdir(INPUT_FOLDER):

#     if file.lower().endswith(".pdf"):

#         suffix = uuid.uuid4().hex[:3].upper()

#         input_path = os.path.join(INPUT_FOLDER, file)
#         output_path = os.path.join(OUTPUT_FOLDER, f"wm_{file}")

#         watermark_existing_pdf(
#             input_pdf=input_path,
#             question_id=question_id,
#             suffix=suffix,
#             output_pdf=output_path
#         )

#         print(f"Watermarked: {file}")

import sys
import os
import uuid

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.utils.text_extractor import extract_text
from app.watermark.embed import generate_pdf_from_text


INPUT_FOLDER = "documents"
OUTPUT_FOLDER = "watermarked"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

question_id = "TS-Q-2026-001"

for filename in os.listdir(INPUT_FOLDER):

    if filename.lower().endswith((".pdf", ".docx")):

        input_path = os.path.join(INPUT_FOLDER, filename)

        with open(input_path, "rb") as f:
            file_bytes = f.read()

        text = extract_text(file_bytes, filename)

        suffix = uuid.uuid4().hex[:3].upper()

        output_filename = f"wm_{filename.replace('.pdf','').replace('.docx','')}.pdf"

        output_path = os.path.join(OUTPUT_FOLDER, output_filename)

        generate_pdf_from_text(
            text,
            question_id,
            suffix,
            output_path
        )

        print(f"Watermarked: {filename} → {output_filename}")