"use client";

import { useState } from "react";
import { UploadCard } from "@/components/UploadCard";
import { ResultCard } from "@/components/ResultCard";
import { apiMultipart, type CheckCopyResponse } from "@/lib/api";

interface BackendAnalysis {
  status?: string;
  classification?: string;
  similarity_score?: number;
  watermark?: string | null;
  matched_question?: string | null;
  watermark_detected?: boolean;
}

export default function DetectCopyPage() {
  const [isAnalyzing, setIsAnalyzing] = useState(false);
  const [result, setResult] = useState<CheckCopyResponse | null>(null);
  const [error, setError] = useState("");

  const handleUpload = async (file: File) => {
    setIsAnalyzing(true);
    setError("");
    setResult(null);

    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await apiMultipart.post<{ results?: { analysis?: BackendAnalysis }[] }>(
        "/check-copy",
        formData,
        {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        }
      );
      console.log("Backend response:", response.data);

      // Extract FIRST analysis result
      const analysis = response.data?.results?.[0]?.analysis;

      if (!analysis) {
        throw new Error("No analysis result returned");
      }

      setResult({
        classification: (analysis.classification || analysis.status || "UNKNOWN") as CheckCopyResponse["classification"],
        similarity_score: analysis.similarity_score || (analysis.status === "EXACT_COPY" ? 1 : 0),
        matched_question: analysis.matched_question || null,
        watermark_detected: !!analysis.watermark || analysis.watermark_detected || false,
      });
    } catch (err) {
      const error = err as { response?: { data?: { detail?: string } }, message?: string };
      console.error("Analysis error:", error);
      setError(
        error.response?.data?.detail || error.message || "Failed to analyze document. Ensure backend is running."
      );
    } finally {
      setIsAnalyzing(false);
    }
  };

  return (
    <div className="container mx-auto px-4 py-12 sm:px-6 lg:px-8 max-w-5xl">
      <div className="mb-12 text-center">
        <h1 className="text-3xl font-extrabold text-slate-900 sm:text-4xl">
          Analyze Document
        </h1>
        <p className="mt-4 text-lg text-slate-600 max-w-2xl mx-auto">
          Upload a question paper to detect exact copies, modified versions, and verify internal watermarks.
        </p>
      </div>

      <div className="space-y-8">
        <UploadCard onUpload={handleUpload} isLoading={isAnalyzing} />

        {error && (
          <div className="max-w-2xl mx-auto p-4 bg-red-50 border border-red-200 text-red-600 rounded-xl text-center shadow-sm">
            {error}
          </div>
        )}

        {result && <ResultCard result={result} />}
      </div>
    </div>
  );
}
