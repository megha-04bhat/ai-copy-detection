import faiss
import numpy as np
import json
import os

from app.similarity.model import model

# ---------------------------------------------------
# CONFIGURATION
# ---------------------------------------------------

DIMENSION = 768  # For all-mpnet-base-v2
INDEX_PATH = "data/faiss.index"
QUESTIONS_PATH = "data/questions.json"

# Global objects
index = None
question_store = []


# ---------------------------------------------------
# INITIALIZATION
# ---------------------------------------------------

def initialize_index():
    """
    Initializes FAISS index.
    Loads existing index from disk if available.
    Otherwise creates new one.
    """
    global index, question_store

    # Create data folder if not exists
    os.makedirs("data", exist_ok=True)

    if os.path.exists(INDEX_PATH) and os.path.exists(QUESTIONS_PATH):
        index = faiss.read_index(INDEX_PATH)

        with open(QUESTIONS_PATH, "r") as f:
            question_store = json.load(f)

        print("FAISS index loaded from disk.")
        print(f"Total stored questions: {index.ntotal}")

    else:
        # Cosine similarity → use Inner Product with normalized vectors
        index = faiss.IndexFlatIP(DIMENSION)
        question_store = []

        print("New FAISS index created.")


# ---------------------------------------------------
# SAVE TO DISK
# ---------------------------------------------------

def save_index():
    """
    Saves FAISS index and question store to disk.
    """
    faiss.write_index(index, INDEX_PATH)

    with open(QUESTIONS_PATH, "w") as f:
        json.dump(question_store, f, indent=2)

    print("FAISS index saved to disk.")


# ---------------------------------------------------
# ADD QUESTION
# ---------------------------------------------------

def add_question(question_text: str):
    """
    Adds new question to FAISS index and saves it.
    """
    global index, question_store

    if index is None:
        raise Exception("FAISS index not initialized. Call initialize_index() first.")

    # Generate normalized embedding
    embedding = model.encode(question_text, normalize_embeddings=True)
    embedding = np.array([embedding]).astype("float32")

    # Add to FAISS
    index.add(embedding)

    # Store text mapping
    question_store.append(question_text)

    # Persist to disk
    save_index()

    print(f"Question added. Total questions: {index.ntotal}")


# ---------------------------------------------------
# SEARCH SIMILAR
# ---------------------------------------------------

def search_similar(text: str, k: int = 1):
    """
    Searches FAISS for most similar question.

    Returns:
        matched_question (str or None)
        similarity_score (float)
    """
    global index, question_store

    if index is None:
        raise Exception("FAISS index not initialized.")

    if index.ntotal == 0:
        return None, 0.0

    # Encode input text
    embedding = model.encode(text, normalize_embeddings=True)
    embedding = np.array([embedding]).astype("float32")

    # Search FAISS
    scores, indices = index.search(embedding, k=k)

    best_score = float(scores[0][0])
    best_index = indices[0][0]

    if best_index == -1:
        return None, 0.0

    matched_question = question_store[best_index]

    return matched_question, best_score


# ---------------------------------------------------
# OPTIONAL: CLEAR INDEX (FOR TESTING)
# ---------------------------------------------------

def clear_index():
    """
    Clears FAISS index and deletes stored files.
    Useful for testing/resetting system.
    """
    global index, question_store

    index = faiss.IndexFlatIP(DIMENSION)
    question_store = []

    if os.path.exists(INDEX_PATH):
        os.remove(INDEX_PATH)

    if os.path.exists(QUESTIONS_PATH):
        os.remove(QUESTIONS_PATH)

    print("FAISS index cleared.")