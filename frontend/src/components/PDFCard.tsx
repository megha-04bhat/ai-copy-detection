import { FileText, Download, CheckCircle2 } from "lucide-react";

interface PDFCardProps {
  onDownload: () => void;
}

export function PDFCard({ onDownload }: PDFCardProps) {
  return (
    <div className="w-full max-w-md mx-auto mt-8 bg-white rounded-3xl shadow-xl border border-gray-100 overflow-hidden animate-in zoom-in-95 duration-500">
      <div className="bg-gradient-to-br from-blue-500 to-blue-700 p-8 text-center relative overflow-hidden">
        {/* Abstract background shapes */}
        <div className="absolute -top-10 -right-10 w-32 h-32 bg-white/10 rounded-full blur-2xl"></div>
        <div className="absolute -bottom-10 -left-10 w-32 h-32 bg-white/10 rounded-full blur-2xl"></div>
        
        <div className="relative z-10 flex flex-col items-center">
          <div className="w-16 h-16 bg-white/20 backdrop-blur-sm rounded-2xl flex items-center justify-center mb-4 text-white">
            <FileText className="w-8 h-8" />
          </div>
          <h3 className="text-xl font-bold text-white mb-1">Paper Generated</h3>
          <p className="text-blue-100 text-sm">Successfully created and watermarked.</p>
        </div>
      </div>
      
      <div className="p-8">
        <div className="flex items-center gap-3 mb-6 text-sm text-gray-600 bg-green-50 text-green-700 p-3 rounded-xl border border-green-100">
          <CheckCircle2 className="w-5 h-5" />
          <span>Invisible tracking watermark applied</span>
        </div>
        
        <button
          onClick={onDownload}
          className="w-full py-4 px-6 bg-slate-900 hover:bg-slate-800 text-white rounded-xl font-medium flex items-center justify-center gap-2 transition-all hover:shadow-lg active:scale-[0.98]"
        >
          <Download className="w-5 h-5" />
          Download PDF
        </button>
      </div>
    </div>
  );
}
