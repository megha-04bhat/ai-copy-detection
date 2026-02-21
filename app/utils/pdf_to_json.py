import re


def convert_text_to_json(extracted_text: str):
    """
    Extracts questions using structural heuristics
    instead of strict regex patterns.
    Works for unknown numbering formats.
    """

    # Normalize line endings
    text = extracted_text.replace("\r", "").strip()

    # Split by newline first
    lines = text.split("\n")

    questions = []
    current_question = []
    question_number = 1

    def looks_like_new_question(line: str):
        """
        Detect if line likely starts a new question.
        Heuristic-based detection.
        """

        line = line.strip()

        if not line:
            return False

        # Case 1: Starts with number (1, 2, 10, etc.)
        if re.match(r"^\d+", line):
            return True

        # Case 2: Starts with uppercase letter + period
        if re.match(r"^[A-Z]\.", line):
            return True

        # Case 3: Contains question mark and is standalone
        if "?" in line and len(line) < 200:
            return True

        # Case 4: Starts with Q/q followed by anything
        if line.lower().startswith("q"):
            return True

        return False

    for line in lines:
        line = line.strip()

        if not line:
            continue

        if looks_like_new_question(line):
            # Save previous question
            if current_question:
                questions.append({
                    "question_number": question_number,
                    "question_text": " ".join(current_question).strip()
                })
                question_number += 1
                current_question = []

        current_question.append(line)

    # Add last question
    if current_question:
        questions.append({
            "question_number": question_number,
            "question_text": " ".join(current_question).strip()
        })

    return {
        "questions": questions
    }