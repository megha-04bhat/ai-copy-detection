from app.similarity.compare import calculate_similarity, classify_similarity
# from app.config import MODEL_NAME
# from app.similarity.model import model

text1 = """
Explain Newton's First Law of Motion in detail.
Discuss its statement, assumptions, and real-world applications.
"""

text2 = """
Describe Newton's First Law, also known as the Law of Inertia.
Explain how it applies to everyday motion.
"""


score = calculate_similarity(text1, text2)
similarity = classify_similarity(score)

print("Similarity score:", score)
print("Classification:", similarity)
# print("Loaded model:", MODEL_NAME)
# print(len(model.encode("test")))

