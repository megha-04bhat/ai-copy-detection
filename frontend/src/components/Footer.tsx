export function Footer() {
  return (
    <footer className="border-t border-gray-200/50 bg-slate-50/50 backdrop-blur-sm mt-auto">
      <div className="container mx-auto px-4 py-8 sm:px-6 lg:px-8">
        <div className="flex flex-col md:flex-row items-center justify-between gap-4">
          <div className="flex items-center gap-2">
            <span className="text-lg font-bold tracking-tight text-slate-800">
              AuraDetect
            </span>
            <span className="text-sm text-slate-500">
              © {new Date().getFullYear()} All rights reserved.
            </span>
          </div>
          <div className="flex gap-6 text-sm text-slate-500">
            <a href="#" className="hover:text-blue-600 transition-colors">Privacy</a>
            <a href="#" className="hover:text-blue-600 transition-colors">Terms</a>
            <a href="#" className="hover:text-blue-600 transition-colors">Documentation</a>
          </div>
        </div>
      </div>
    </footer>
  );
}
