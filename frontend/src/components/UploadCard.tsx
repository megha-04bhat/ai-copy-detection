"use client";

import { useCallback, useState } from "react";
import { useDropzone } from "react-dropzone";
import { UploadCloud, File, X } from "lucide-react";
import { cn } from "@/lib/utils";

interface UploadCardProps {
  onUpload: (file: File) => void;
  isLoading: boolean;
}

export function UploadCard({ onUpload, isLoading }: UploadCardProps) {
  const [selectedFile, setSelectedFile] = useState<File | null>(null);

  const onDrop = useCallback((acceptedFiles: File[]) => {
    if (acceptedFiles.length > 0) {
      setSelectedFile(acceptedFiles[0]);
    }
  }, []);

  const { getRootProps, getInputProps, isDragActive } = useDropzone({
    onDrop,
    accept: {
      "application/pdf": [".pdf"],
      "application/vnd.openxmlformats-officedocument.wordprocessingml.document": [".docx"],
    },
    maxFiles: 1,
    disabled: isLoading,
  });

  const handleUploadClick = (e: React.MouseEvent) => {
    e.stopPropagation();
    if (selectedFile) {
      onUpload(selectedFile);
    }
  };

  const removeFile = (e: React.MouseEvent) => {
    e.stopPropagation();
    setSelectedFile(null);
  };

  return (
    <div className="w-full max-w-2xl mx-auto">
      <div
        {...getRootProps()}
        className={cn(
          "relative overflow-hidden rounded-2xl border-2 border-dashed p-10 transition-all duration-300 ease-in-out cursor-pointer",
          isDragActive
            ? "border-blue-500 bg-blue-50/50 scale-[1.02]"
            : "border-gray-300 bg-white hover:border-blue-400 hover:bg-gray-50",
          isLoading && "opacity-60 pointer-events-none"
        )}
      >
        <input {...getInputProps()} />
        
        <div className="flex flex-col items-center justify-center space-y-4 text-center">
          {!selectedFile ? (
            <>
              <div className="p-4 rounded-full bg-blue-100/50 text-blue-600 mb-2">
                <UploadCloud className="w-10 h-10" />
              </div>
              <div className="space-y-1">
                <p className="text-xl font-semibold text-gray-800">
                  Click or drag file to this area to upload
                </p>
                <p className="text-sm text-gray-500">
                  Support for a single PDF or DOCX file
                </p>
              </div>
            </>
          ) : (
            <div className="w-full">
              <div className="flex items-center p-4 bg-white border rounded-xl shadow-sm">
                <div className="p-2 bg-blue-50 rounded-lg text-blue-600 mr-4">
                  <File className="w-8 h-8" />
                </div>
                <div className="flex-1 text-left truncate mr-4">
                  <p className="text-sm font-medium text-gray-900 truncate">
                    {selectedFile.name}
                  </p>
                  <p className="text-xs text-gray-500">
                    {(selectedFile.size / 1024 / 1024).toFixed(2)} MB
                  </p>
                </div>
                {!isLoading && (
                  <button
                    onClick={removeFile}
                    className="p-2 text-gray-400 hover:text-red-500 transition-colors"
                  >
                    <X className="w-5 h-5" />
                  </button>
                )}
              </div>
              
              <button
                onClick={handleUploadClick}
                disabled={isLoading}
                className={cn(
                  "mt-6 w-full py-3 px-4 rounded-xl font-medium text-white transition-all duration-200",
                  isLoading
                    ? "bg-blue-400 cursor-not-allowed"
                    : "bg-blue-600 hover:bg-blue-700 hover:shadow-lg active:scale-[0.98]"
                )}
              >
                {isLoading ? (
                  <span className="flex items-center justify-center gap-2">
                    <svg className="animate-spin h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                      <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                      <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                    </svg>
                    Analyzing Document...
                  </span>
                ) : (
                  "Run Copy Detection"
                )}
              </button>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
