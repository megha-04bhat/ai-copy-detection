from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import os


def generate_watermark(question_id: str, suffix: str) -> str:
    """
    Generates watermark string.
    Example:
    QID:TS-Q-2026-001-A9X
    """
    return f"QID:{question_id}-{suffix}"


def generate_question_pdf(
    question_text: str,
    question_id: str,
    suffix: str,
    output_path: str = "generated_question.pdf"
):
    """
    Generates PDF with invisible watermark embedded.
    """

    c = canvas.Canvas(output_path, pagesize=A4)
    width, height = A4

    # 1️⃣ Visible Question
    c.setFont("Helvetica", 12)
    c.drawString(50, height - 100, question_text)

    # 2️⃣ Invisible Watermark
    watermark = generate_watermark(question_id, suffix)

    c.setFont("Helvetica", 1)  # tiny font
    c.setFillColorRGB(1, 1, 1)  # white color
    c.drawString(50, height - 110, watermark)

    c.save()

    return output_path
