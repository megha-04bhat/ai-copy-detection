from app.watermark.embed import generate_pdf_from_text

# generate_pdf_from_text(
#     question_text="Explain Newton's First Law",
#     question_id="TS-Q-2026-001",
#     suffix="A9X",
#     output_path="sample_question.pdf"
# )

# print("PDF generated successfully")
text = """
1. Explain Newton's First Law of Motion.
2. Define Ohm's Law with example.
3. What is Artificial Intelligence?
"""

question_id = "TS-Q-2026-001"

suffix = "A9X"

output_file = "tests/generated_question.pdf"

generate_pdf_from_text(
    text,
    question_id,
    suffix,
    output_file
)

print("PDF generated:", output_file)