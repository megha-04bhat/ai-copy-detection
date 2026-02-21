# from app.watermark.detect import detect_watermark
from app.similarity.compare import calculate_similarity, classify_similarity
from app.similarity.faiss_index import search_similar

# def evaluate_document(extracted_text: str, database_questions: list):
#     """
#     Runs watermark detection and semantic similarity,
#     then returns final classification.
#     """

#     # Step 1: Watermark Detection (Highest Priority)
#     watermark_found, watermark_value = detect_watermark(extracted_text)

#     if watermark_found:
#         return {
#             "status": "EXACT_COPY",
#             "watermark": watermark_value,
#             "similarity_score": None,
#             "matched_question": None
#         }

#     # Step 2: Semantic Similarity
#     highest_score = 0
#     matched_question = None

#     for question in database_questions:
#         score = calculate_similarity(extracted_text, question)

#         if score > highest_score:
#             highest_score = score
#             matched_question = question

#     classification = classify_similarity(highest_score)

#     return {
#         "status": classification,
#         "watermark": None,
#         "similarity_score": highest_score,
#         "matched_question": matched_question
#     }


def evaluate_document(extracted_text: str):

    # watermark_found, watermark_value = detect_watermark(extracted_text)

    # if watermark_found:
    #     return {
    #         "status": "EXACT_COPY",
    #         "watermark": watermark_value,
            
    #     }

    matched_question, score = search_similar(extracted_text)

    classification = classify_similarity(score)

    return {
        "status": classification,
        "similarity_score": score,
        "matched_question": matched_question
    }


