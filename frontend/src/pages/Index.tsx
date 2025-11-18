import { FileUpload } from "@/components/FileUpload";
import { ChatInterface } from "@/components/ChatInterface";
import { BookOpen } from "lucide-react";

const Index = () => {
  return (
    <div className="min-h-screen relative overflow-hidden">
      {/* Deep space background gradient - unique atmospheric effect */}
      <div className="fixed inset-0 bg-gradient-to-br from-slate-950 via-purple-950 to-slate-900" />
      <div className="fixed inset-0 bg-[radial-gradient(circle_at_20%_30%,hsl(260_90%_40%/0.2),transparent_40%)]" />
      <div className="fixed inset-0 bg-[radial-gradient(circle_at_80%_70%,hsl(340_90%_50%/0.15),transparent_40%)]" />
      <div className="fixed inset-0 bg-[radial-gradient(circle_at_50%_50%,hsl(280_70%_50%/0.1),transparent_60%)]" />
      
      <div className="relative z-10">
        <header className="border-b border-border/50 bg-card/60 backdrop-blur-xl sticky top-0 z-20 shadow-sm">
        <div className="container mx-auto px-4 py-4">
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 rounded-xl bg-gradient-to-br from-primary to-accent flex items-center justify-center">
              <BookOpen className="w-6 h-6 text-white" />
            </div>
            <div>
              <h1 className="text-2xl font-bold bg-gradient-to-r from-primary to-accent bg-clip-text text-transparent">
                RAG Chatbot
              </h1>
              <p className="text-sm text-muted-foreground">
                Upload documents and ask questions
              </p>
            </div>
          </div>
        </div>
      </header>

        <main className="container mx-auto px-4 py-6">
          <div className="grid lg:grid-cols-[400px_1fr] gap-6 h-[calc(100vh-140px)]">
            {/* Document Library with unique blue-indigo gradient */}
            <div className="relative bg-gradient-to-br from-indigo-950/80 via-purple-900/60 to-indigo-950/80 rounded-xl border border-indigo-500/30 p-6 shadow-2xl backdrop-blur-md overflow-hidden">
              <div className="absolute inset-0 bg-gradient-to-br from-indigo-500/10 via-transparent to-purple-500/10 pointer-events-none" />
              <div className="absolute inset-0 bg-[radial-gradient(circle_at_30%_30%,hsl(250_80%_60%/0.15),transparent_50%)] pointer-events-none" />
              <div className="relative z-10">
                <h2 className="text-lg font-semibold mb-4 flex items-center gap-2">
                  <div className="w-2 h-2 rounded-full bg-gradient-to-r from-indigo-400 to-purple-400 animate-pulse" />
                  Document Library
                </h2>
                <FileUpload />
              </div>
            </div>

            {/* Chat Interface with unique pink-fuchsia gradient */}
            <div className="relative bg-gradient-to-br from-pink-950/80 via-fuchsia-900/60 to-pink-950/80 rounded-xl border border-pink-500/30 shadow-2xl backdrop-blur-md overflow-hidden">
              <div className="absolute inset-0 bg-gradient-to-tl from-fuchsia-500/10 via-transparent to-pink-500/10 pointer-events-none" />
              <div className="absolute inset-0 bg-[radial-gradient(circle_at_70%_70%,hsl(320_80%_60%/0.15),transparent_50%)] pointer-events-none" />
              <div className="relative z-10 h-full">
                <ChatInterface />
              </div>
            </div>
          </div>
        </main>
      </div>
    </div>
  );
};

export default Index;
