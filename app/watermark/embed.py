# from reportlab.pdfgen import canvas
# from reportlab.lib.pagesizes import A4
# from reportlab.graphics import renderPDF
# from svglib.svglib import svg2rlg
# from app.config import SVG_FILE
# from pypdf import PdfReader, PdfWriter
# from pdf2image import convert_from_path
# import tempfile
# import os
# import cv2
# import numpy as np


# def generate_watermark(question_id: str, suffix: str) -> str:
#     """
#     Generates watermark string.
#     Example:
#     QID:TS-Q-2026-001-A9X
#     """
#     return f"QID:{question_id}-{suffix}"

# def detect_watermark_position(pdf_path):

#     page = convert_from_path(pdf_path, first_page=1, last_page=1)[0]

#     img = cv2.cvtColor(np.array(page), cv2.COLOR_BGR2GRAY)

#     edges = cv2.Canny(img, 50, 150)

#     coords = np.column_stack(np.where(edges > 0))

#     if len(coords) == 0:
#         return 300, 400   # fallback position

#     y, x = coords.mean(axis=0)

#     return int(x), int(y)


# def generate_question_pdf(
#     question_text: str,
#     question_id: str,
#     suffix: str,
#     output_path: str = "generated_question.pdf"
# ):
#     """
#     Generates PDF with invisible watermark embedded.
#     """

#     c = canvas.Canvas(output_path, pagesize=A4)
#     width, height = A4
    
    
#     if os.path.exists(SVG_FILE):
#         drawing = svg2rlg(SVG_FILE)
#         drawing.width = drawing.width*0.5
#         drawing.height = drawing.height*0.5
#         renderPDF.draw(drawing, c , width/2-100, height/2)

#     # 1️⃣ Visible Question
#     c.setFont("Helvetica", 12)
#     c.drawString(50, height - 100, question_text)

#     # 2️⃣ Invisible Watermark
#     watermark = generate_watermark(question_id, suffix)

#     c.setFont("Helvetica", 1)  # tiny font
#     c.setFillColorRGB(1, 1, 1)  # white color
#     c.drawString(50, height - 110, watermark)

#     c.save()

#     return output_path

# # def watermark_existing_pdf(
# #         input_pdf: str,
# #         question_id: str,
# #         suffix: str,
# #         output_pdf: str
# # ):
# #     """
# #     Apply watermark to an existing PDF (handwritten notes).
# #     """

# #     watermark = generate_watermark(question_id, suffix)

# #     # Create temporary overlay PDF
# #     temp_overlay = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
# #     x, y = detect_watermark_position(input_pdf)

# #     c = canvas.Canvas(temp_overlay.name, pagesize=A4)
# #     width, height = A4

# #     # SVG logo watermark
# #     if os.path.exists(SVG_FILE):
# #         drawing = svg2rlg(SVG_FILE)
# #         drawing.width *= 0.7
# #         drawing.height *= 0.7
# #         c.saveState()

# #     # move origin to center of page
# #         c.translate(x, y)

# #     # rotate watermark diagonally
# #         c.rotate(45)

# #     # draw watermark centered
# #         renderPDF.draw(drawing, c, -250, -50)

# #     # restore canvas state
# #         c.restoreState()

# #     # Hidden text watermark
# #     c.setFont("Helvetica", 1)
# #     c.setFillColorRGB(1, 1, 1)
# #     c.drawString(10, 10, watermark)

# #     c.save()

# #     # Read PDFs
# #     reader = PdfReader(input_pdf)
# #     overlay_reader = PdfReader(temp_overlay.name)

# #     writer = PdfWriter()

# #     overlay_page = overlay_reader.pages[0]

# #     # for page in reader.pages:
# #     #     watermark_layer = overlay_reader.pages[0]

# #     #     # watermark behind content
# #     #     watermark_layer.merge_page(page)

# #     #     writer.add_page(watermark_layer)

# #     # with open(output_pdf, "wb") as f:
# #     #     writer.write(f)

# #     # return output_pdf
# #     for page in reader.pages:

# #         page.merge_page(overlay_page)

# #         writer.add_page(page)

# #     with open(output_pdf, "wb") as f:
# #         writer.write(f)

# #     return output_pdf
# def watermark_existing_pdf(input_pdf: str, question_id: str, suffix: str, output_pdf: str):

#     watermark = generate_watermark(question_id, suffix)

#     temp_overlay = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
#     temp_overlay.close()

#     x, y = detect_watermark_position(input_pdf)

#     c = canvas.Canvas(temp_overlay.name, pagesize=A4)

#     width, height = A4

#     if os.path.exists(SVG_FILE):

#         drawing = svg2rlg(SVG_FILE)

#         scale = width / drawing.width * 0.8

#         drawing.width *= scale
#         drawing.height *= scale
#         c.saveState()

#         c.translate(x, y)

#         c.rotate(45)

#         renderPDF.draw(drawing, c, -250, -50)

#         c.restoreState()

#     c.setFont("Helvetica", 1)
#     c.setFillColorRGB(1,1,1)

#     c.drawString(10,10, watermark)

#     c.save()
    

#     reader = PdfReader(input_pdf)

#     overlay_reader = PdfReader(temp_overlay.name)

#     overlay_page = overlay_reader.pages[0]

#     writer = PdfWriter()

#     for page in reader.pages:

#         page.merge_page(overlay_page)

#         writer.add_page(page)

#     with open(output_pdf, "wb") as f:
#         writer.write(f)

#     os.remove(temp_overlay.name)

#     return output_pdf

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.graphics import renderPDF
from reportlab.lib.utils import ImageReader
#from svglib.svglib import svg2rlg
from app.config import PNG_FILE
import os


def generate_watermark(question_id: str, suffix: str) -> str:
    return f"QID:{question_id}-{suffix}"

def draw_watermark(c, width, height):
    logo = ImageReader(PNG_FILE)
    img_w, img_h = logo.getSize()
    scale = min(width/img_w, height/img_h) * 0.65
    w = img_w * scale
    h = img_h * scale
    c.saveState()
    c.setFillAlpha(0.12)

    c.translate(width/2, height/2)
    c.rotate(45)
    c.drawImage(
        logo, -w/2, -h/2, w, h, mask='auto'
    )
    c.restoreState()
def generate_pdf_from_text(
        text: str,
        question_id: str,
        suffix: str,
        output_path: str
):
    """
    Generates a new PDF from extracted text
    and applies SVG watermark + hidden watermark.
    """

    watermark = generate_watermark(question_id, suffix)

    c = canvas.Canvas(output_path, pagesize=A4)

    width, height = A4
    draw_watermark(c, width, height)

    # -------------------
    # SVG Watermark
    # -------------------
    # if os.path.exists(SVG_FILE):

    #     drawing = svg2rlg(SVG_FILE)

    # # original SVG size
    #     svg_w = drawing.width
    #     svg_h = drawing.height

    # # page size
    #     page_w = width
    #     page_h = height

    # # scale watermark relative to page
    #     scale = min(page_w / svg_w, page_h / svg_h) * 0.9

    #     drawing.width = svg_w * scale
    #     drawing.height = svg_h * scale

    #     c.saveState()

    # # always place watermark at center
    #     c.translate(page_w / 2, page_h / 2)

    # # rotate watermark (typical exam watermark style)
    #     c.rotate(45)

    # # draw centered
    #     renderPDF.draw(
    #     drawing,
    #     c,
    #     -drawing.width / 2,
    #     -drawing.height / 2
    #     )

    #     c.restoreState()

    # -------------------
    # Write extracted text
    # -------------------

    y = height - 80
    c.setFont("Helvetica", 12)

    for line in text.split("\n"):

        if y < 60:
            c.showPage()
            draw_watermark(c, width, height)
            y = height - 80
            c.setFont("Helvetica", 12)

        c.drawString(50, y, line)
        y -= 18

    # -------------------
    # Hidden watermark
    # -------------------

    c.setFont("Helvetica", 1)
    c.setFillColorRGB(1, 1, 1)

    c.drawString(10, 10, watermark)

    c.save()

    return output_path