import axios from "axios";

// Assume the backend is running on http://127.0.0.1:8000
const API_BASE_URL = "http://127.0.0.1:8000";

export const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    "Content-Type": "application/json",
  },
});

export const apiMultipart = axios.create({
  baseURL: API_BASE_URL,
});

export interface GeneratePaperRequest {
  subject: string;
  difficulty: string;
  num_questions: number;
}

// Interfaces for response typings (assuming based on standard implementations)
export interface CheckCopyResponse {
  classification: "EXACT_COPY" | "MODIFIED_COPY" | "NEW_QUESTION";
  similarity_score: number;
  watermark_detected: boolean;
  matched_question: string | null;
}
