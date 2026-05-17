"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import { FileSearch, FileText } from "lucide-react";
import { cn } from "@/lib/utils";

export function Navbar() {
  const pathname = usePathname();

  const links = [
    // { href: "/generate-paper", label: "Generate Paper", icon: FileText },
    { href: "/detect-copy", label: "Detect Copy", icon: FileSearch },
  ];

  return (
    <nav className="sticky top-0 z-50 w-full border-b border-gray-200/50 bg-white/70 backdrop-blur-md">
      <div className="container mx-auto flex h-16 items-center justify-between px-4 sm:px-6 lg:px-8">
        <Link href="/" className="flex items-center gap-2 group">
          <div className="flex h-8 w-8 items-center justify-center rounded-lg bg-blue-600 text-white transition-transform group-hover:scale-105">
            <FileSearch size={18} />
          </div>
          <span className="text-xl font-bold tracking-tight text-slate-900">
            CopyDetect
          </span>
        </Link>
        <div className="flex items-center gap-6">
          {links.map(({ href, label, icon: Icon }) => (
            <Link
              key={href}
              href={href}
              className={cn(
                "flex items-center gap-2 text-sm font-medium transition-colors hover:text-blue-600 relative",
                pathname === href ? "text-blue-600" : "text-slate-600"
              )}
            >
              <Icon size={16} />
              {label}
              {pathname === href && (
                <span className="absolute -bottom-[22px] left-0 h-[2px] w-full bg-blue-600 rounded-t-full" />
              )}
            </Link>
          ))}
        </div>
      </div>
    </nav>
  );
}
