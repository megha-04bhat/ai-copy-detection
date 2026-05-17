import { CheckCircle2, AlertTriangle, XCircle, FileSearch, Fingerprint } from "lucide-react";
import { cn } from "@/lib/utils";
import type { CheckCopyResponse } from "@/lib/api";

interface ResultCardProps {
  result: CheckCopyResponse;
}

export function ResultCard({ result }: ResultCardProps) {
  const getStatusColor = (classification: string) => {
    switch (classification) {
      case "EXACT_COPY":
        return "bg-red-500/10 text-red-700 border-red-200";
      case "MODIFIED_COPY":
        return "bg-orange-500/10 text-orange-700 border-orange-200";
      case "NEW_QUESTION":
        return "bg-green-500/10 text-green-700 border-green-200";
      default:
        return "bg-gray-100 text-gray-700 border-gray-200";
    }
  };

  const getStatusIcon = (classification: string) => {
    switch (classification) {
      case "EXACT_COPY":
        return <XCircle className="w-6 h-6 text-red-600" />;
      case "MODIFIED_COPY":
        return <AlertTriangle className="w-6 h-6 text-orange-600" />;
      case "NEW_QUESTION":
        return <CheckCircle2 className="w-6 h-6 text-green-600" />;
      default:
        return null;
    }
  };

  const classification = result?.classification || "UNKNOWN";

  const formattedLabel = classification.replaceAll("_", " ");

  return (
    <div className="w-full max-w-2xl mx-auto mt-8 bg-white/80 backdrop-blur-xl border border-white/40 shadow-2xl rounded-3xl overflow-hidden animate-in fade-in slide-in-from-bottom-4 duration-500">
      <div className="p-8">
        <div className="flex items-start justify-between mb-8">
          <div>
            <h3 className="text-sm font-semibold tracking-wider text-gray-500 uppercase mb-2">
              Analysis Result
            </h3>
            <div className="flex items-center gap-3">
              {getStatusIcon(result.classification)}
              <span className="text-2xl font-bold text-gray-900">
                {formattedLabel}
              </span>
            </div>
          </div>
          <div className={cn(
            "px-4 py-2 rounded-full border text-sm font-semibold tracking-wide flex items-center gap-2",
            getStatusColor(result.classification)
          )}>
            {formattedLabel}
          </div>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mb-8">
          <div className="bg-slate-50 rounded-2xl p-6 border border-slate-100">
            <div className="flex items-center gap-2 text-slate-600 mb-4">
              <FileSearch className="w-5 h-5" />
              <span className="font-medium">Similarity Score</span>
            </div>
            <div className="flex items-baseline gap-2">
              <span className="text-4xl font-black text-slate-800">
                {(result.similarity_score * 100).toFixed(1)}
              </span>
              <span className="text-lg text-slate-500 font-medium">%</span>
            </div>

            {/* Confidence Meter */}
            <div className="w-full h-2 bg-slate-200 rounded-full mt-4 overflow-hidden">
              <div
                className={cn(
                  "h-full rounded-full transition-all duration-1000 ease-out",
                  result.similarity_score > 0.8 ? "bg-red-500" : result.similarity_score > 0.4 ? "bg-orange-500" : "bg-green-500"
                )}
                style={{ width: `${result.similarity_score * 100}%` }}
              />
            </div>
          </div>

          <div className="bg-slate-50 rounded-2xl p-6 border border-slate-100">
            <div className="flex items-center gap-2 text-slate-600 mb-4">
              <Fingerprint className="w-5 h-5" />
              <span className="font-medium">Watermark Status</span>
            </div>
            <div className="flex items-center gap-3 mt-2">
              {result.watermark_detected ? (
                <>
                  <div className="p-2 bg-red-100 text-red-600 rounded-full">
                    <AlertTriangle className="w-6 h-6" />
                  </div>
                  <div>
                    <p className="font-bold text-slate-800">Detected</p>
                    <p className="text-sm text-slate-500">Internal Document</p>
                  </div>
                </>
              ) : (
                <>
                  <div className="p-2 bg-green-100 text-green-600 rounded-full">
                    <CheckCircle2 className="w-6 h-6" />
                  </div>
                  <div>
                    <p className="font-bold text-slate-800">Not Found</p>
                    <p className="text-sm text-slate-500">External Origin</p>
                  </div>
                </>
              )}
            </div>
          </div>
        </div>

        {result.matched_question && (
          <div className="border-t border-gray-100 pt-6">
            <h4 className="text-sm font-semibold text-gray-900 mb-3">Matched Question Fragment:</h4>
            <div className="bg-yellow-50/50 border border-yellow-100 rounded-xl p-4 text-sm text-gray-700 italic">
              &quot;{result.matched_question}&quot;
            </div>
          </div>
        )}
      </div>
    </div>
  );
}
