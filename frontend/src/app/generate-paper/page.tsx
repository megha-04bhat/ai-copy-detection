// "use client";

// import { useState } from "react";
// import { FileText, Loader2, Sparkles } from "lucide-react";
// import { api } from "@/lib/api";
// import { PDFCard } from "@/components/PDFCard";
// import { cn } from "@/lib/utils";

// export default function GeneratePaperPage() {
//   const [subject, setSubject] = useState("");
//   const [difficulty, setDifficulty] = useState("Medium");
//   const [numQuestions, setNumQuestions] = useState("5");
//   const [isGenerating, setIsGenerating] = useState(false);
//   const [pdfBlob, setPdfBlob] = useState<Blob | null>(null);
//   const [error, setError] = useState("");

//   const handleGenerate = async (e: React.FormEvent) => {
//     e.preventDefault();
//     if (!subject.trim()) {
//       setError("Please enter a subject");
//       return;
//     }

//     setIsGenerating(true);
//     setError("");
//     setPdfBlob(null);

//     try {
//       const response = await api.post(
//         "/generate-paper",
//         {
//           subject,
//           difficulty,
//           num_questions: parseInt(numQuestions),
//         },
//         { responseType: "blob" } // Critical for downloading files
//       );

//       setPdfBlob(response.data);
//     } catch (err) {
//       const error = err as { response?: { data?: { detail?: string } } };
//       console.error("Generation error:", error);
//       setError(
//         error.response?.data?.detail || "Failed to generate paper. Ensure backend is running."
//       );
//     } finally {
//       setIsGenerating(false);
//     }
//   };

//   const handleDownload = () => {
//     if (!pdfBlob) return;
//     const url = window.URL.createObjectURL(new Blob([pdfBlob]));
//     const link = document.createElement("a");
//     link.href = url;
//     link.setAttribute("download", `${subject.replace(/\s+/g, "_")}_Paper.pdf`);
//     document.body.appendChild(link);
//     link.click();
//     link.remove();
//   };

//   return (
//     <div className="container mx-auto px-4 py-12 sm:px-6 lg:px-8 max-w-5xl">
//       <div className="mb-10 text-center">
//         <h1 className="text-3xl font-extrabold text-slate-900 sm:text-4xl">
//           Generate Question Paper
//         </h1>
//         <p className="mt-4 text-lg text-slate-600 max-w-2xl mx-auto">
//           Create AI-generated academic papers with embedded invisible watermarks
//           for secure distribution and tracking.
//         </p>
//       </div>

//       <div className="grid grid-cols-1 lg:grid-cols-2 gap-12">
//         {/* Form Section */}
//         <div className="bg-white p-8 rounded-3xl shadow-sm border border-slate-200">
//           <form onSubmit={handleGenerate} className="space-y-6">
//             <div>
//               <label className="block text-sm font-semibold text-slate-700 mb-2">
//                 Subject Area
//               </label>
//               <input
//                 type="text"
//                 value={subject}
//                 onChange={(e) => setSubject(e.target.value)}
//                 placeholder="e.g., Computer Science, History, Physics"
//                 className="w-full px-4 py-3 rounded-xl border border-slate-300 focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-all outline-none"
//               />
//             </div>

//             <div className="grid grid-cols-2 gap-6">
//               <div>
//                 <label className="block text-sm font-semibold text-slate-700 mb-2">
//                   Difficulty
//                 </label>
//                 <select
//                   value={difficulty}
//                   onChange={(e) => setDifficulty(e.target.value)}
//                   className="w-full px-4 py-3 rounded-xl border border-slate-300 focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-all outline-none bg-white"
//                 >
//                   <option value="Easy">Easy</option>
//                   <option value="Medium">Medium</option>
//                   <option value="Hard">Hard</option>
//                 </select>
//               </div>

//               <div>
//                 <label className="block text-sm font-semibold text-slate-700 mb-2">
//                   No. of Questions
//                 </label>
//                 <input
//                   type="number"
//                   min="1"
//                   max="20"
//                   value={numQuestions}
//                   onChange={(e) => setNumQuestions(e.target.value)}
//                   className="w-full px-4 py-3 rounded-xl border border-slate-300 focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-all outline-none"
//                 />
//               </div>
//             </div>

//             {error && (
//               <div className="p-4 bg-red-50 border border-red-200 text-red-600 rounded-xl text-sm">
//                 {error}
//               </div>
//             )}

//             <button
//               type="submit"
//               disabled={isGenerating || !subject.trim()}
//               className={cn(
//                 "w-full py-4 px-6 rounded-xl font-bold text-white transition-all flex items-center justify-center gap-2",
//                 isGenerating || !subject.trim()
//                   ? "bg-blue-400 cursor-not-allowed"
//                   : "bg-blue-600 hover:bg-blue-700 hover:shadow-lg active:scale-95"
//               )}
//             >
//               {isGenerating ? (
//                 <>
//                   <Loader2 className="w-5 h-5 animate-spin" />
//                   Generating Paper...
//                 </>
//               ) : (
//                 <>
//                   <Sparkles className="w-5 h-5" />
//                   Generate Question Paper
//                 </>
//               )}
//             </button>
//           </form>
//         </div>

//         {/* Result Section */}
//         <div className="flex flex-col items-center justify-center bg-slate-50/50 rounded-3xl border border-slate-200 border-dashed p-8 min-h-[400px]">
//           {!pdfBlob ? (
//             <div className="text-center text-slate-400 animate-in fade-in">
//               <div className="w-20 h-20 bg-slate-100 rounded-full flex items-center justify-center mx-auto mb-4">
//                 <FileText className="w-10 h-10 text-slate-300" />
//               </div>
//               <p>Your generated paper will appear here.</p>
//             </div>
//           ) : (
//             <PDFCard onDownload={handleDownload} />
//           )}
//         </div>
//       </div>
//     </div>
//   );
// }
