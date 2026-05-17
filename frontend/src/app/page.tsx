import Link from "next/link";
import { FileText, FileSearch, ArrowRight, ShieldCheck, Zap, BookOpen } from "lucide-react";

export default function Home() {
  return (
    <div className="flex flex-col min-h-[calc(100vh-4rem)]">
      {/* Hero Section */}
      <section className="relative flex-1 flex flex-col items-center justify-center py-20 px-4 overflow-hidden">
        {/* Background Gradients */}
        <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[800px] h-[800px] bg-blue-100/50 rounded-full blur-3xl opacity-50 pointer-events-none" />
        <div className="absolute top-0 right-0 w-[500px] h-[500px] bg-indigo-100/50 rounded-full blur-3xl opacity-50 pointer-events-none" />
        
        <div className="relative z-10 text-center max-w-4xl mx-auto space-y-8 animate-in fade-in slide-in-from-bottom-8 duration-700">
          <div className="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-blue-50 border border-blue-100 text-blue-700 text-sm font-medium mb-4">
            <ShieldCheck size={16} />
            <span>Advanced Academic Integrity System</span>
          </div>
          
          <h1 className="text-5xl md:text-7xl font-extrabold text-slate-900 tracking-tight leading-tight">
            AI-Powered Academic <br className="hidden md:block" />
            <span className="text-transparent bg-clip-text bg-gradient-to-r from-blue-600 to-indigo-600">
              Copy Detection System
            </span>
          </h1>
          
          <p className="text-xl text-slate-600 max-w-2xl mx-auto leading-relaxed">
            Secure your academic assessments with invisible watermarking and 
            advanced semantic similarity detection powered by FAISS and Sentence Transformers.
          </p>
          
          <div className="flex flex-col sm:flex-row items-center justify-center gap-4 pt-8">
            {/* <Link 
              href="/generate-paper" 
              className="group flex items-center justify-center gap-2 w-full sm:w-auto px-8 py-4 bg-blue-600 hover:bg-blue-700 text-white rounded-xl font-semibold transition-all hover:shadow-lg hover:shadow-blue-600/20 active:scale-95"
            >
              <FileText size={20} />
              Generate Question Paper
            </Link> */}
            <Link 
              href="/detect-copy" 
              className="group flex items-center justify-center gap-2 w-full sm:w-auto px-8 py-4 bg-white border border-slate-200 hover:border-blue-200 hover:bg-blue-50 text-slate-700 hover:text-blue-700 rounded-xl font-semibold transition-all shadow-sm active:scale-95"
            >
              <FileSearch size={20} />
              Detect Copy
              <ArrowRight size={16} className="transition-transform group-hover:translate-x-1" />
            </Link>
          </div>
        </div>
      </section>

      {/* Features Section */}
      <section className="py-20 bg-white border-t border-slate-100 relative z-10">
        <div className="container mx-auto px-4 sm:px-6 lg:px-8">
          <div className="grid grid-cols-1 md:grid-cols-3 gap-10 max-w-6xl mx-auto">
            <div className="p-6 rounded-2xl bg-slate-50 border border-slate-100 transition-all hover:shadow-md">
              <div className="w-12 h-12 bg-blue-100 text-blue-600 rounded-xl flex items-center justify-center mb-6">
                <ShieldCheck size={24} />
              </div>
              <h3 className="text-xl font-bold text-slate-900 mb-3">Invisible Watermarking</h3>
              <p className="text-slate-600 leading-relaxed">
                Embed undetectable watermarks into generated PDFs to trace origin and identify exact unauthorized copies instantly.
              </p>
            </div>
            <div className="p-6 rounded-2xl bg-slate-50 border border-slate-100 transition-all hover:shadow-md">
              <div className="w-12 h-12 bg-indigo-100 text-indigo-600 rounded-xl flex items-center justify-center mb-6">
                <Zap size={24} />
              </div>
              <h3 className="text-xl font-bold text-slate-900 mb-3">Semantic Detection</h3>
              <p className="text-slate-600 leading-relaxed">
                Detect modified or rephrased questions using AI-based vector similarity search even if words are changed.
              </p>
            </div>
            <div className="p-6 rounded-2xl bg-slate-50 border border-slate-100 transition-all hover:shadow-md">
              <div className="w-12 h-12 bg-purple-100 text-purple-600 rounded-xl flex items-center justify-center mb-6">
                <BookOpen size={24} />
              </div>
              <h3 className="text-xl font-bold text-slate-900 mb-3">Academic Standard</h3>
              <p className="text-slate-600 leading-relaxed">
                Generate professionally formatted exam papers with varying difficulty levels tailored to your curriculum.
              </p>
            </div>
          </div>
        </div>
      </section>
    </div>
  );
}
