from app.watermark.embed import generate_question_pdf

generate_question_pdf(
    question_text="Explain Newton's First Law",
    question_id="TS-Q-2026-001",
    suffix="A9X",
    output_path="sample_question.pdf"
)

print("PDF generated successfully")