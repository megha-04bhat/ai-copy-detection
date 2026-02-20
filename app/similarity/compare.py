from sklearn.metrics.pairwise import cosine_similarity
from app.similarity.model import model
from app.config import SIMILARITY_THRESHOLD, HIGH_CONFIDENCE_THRESHOLD
import numpy as np

def calculate_similarity(text1: str, text2: str) -> float:
    embeddings = model.encode([text1, text2], normalize_embeddings=True)

    # score = cosine_similarity(
    #     [embeddings[0]],
    #     [embeddings[1]]
    # )[0][0]
    score = np.dot(embeddings[0], embeddings[1])

    return float(score)

def classify_similarity(score: float):
    if score >= HIGH_CONFIDENCE_THRESHOLD:
        return "HIGH_CONFIDENCE_COPY"
    
    elif score >= SIMILARITY_THRESHOLD:
        return "MODIFIED_COPY"
    
    else:
        return "NEW_QUESTION"