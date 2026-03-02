from app.database.connection import get_connection


def get_all_questions():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT question_id, question_text FROM questions;")
    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return rows