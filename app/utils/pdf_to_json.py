import re


def convert_text_to_json(extracted_text: str):
    """
    Converts question paper text into structured JSON.
    Handles:
    - Q1. ...
    - Q2. ...
    - Multi-line questions
    """

    # Normalize whitespace
    text = re.sub(r"\s+", " ", extracted_text)

    # Pattern to match Q1. Q2. Q10. etc.
    pattern = r"(Q\d+\.)"

    parts = re.split(pattern, text)

    questions = []

    # re.split keeps delimiters, so we process pairs
    for i in range(1, len(parts), 2):
        question_label = parts[i]         # e.g., "Q1."
        question_body = parts[i + 1].strip()

        # Extract question number
        number_match = re.search(r"\d+", question_label)
        if number_match:
            question_number = int(number_match.group())

            questions.append({
                "question_number": question_number,
                "question_text": question_body.strip()
            })

    return {
        "questions": questions
    }