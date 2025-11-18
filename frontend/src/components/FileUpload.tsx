import { useState, useCallback } from "react";
import { Upload, X, File, Loader2 } from "lucide-react";
import { Button } from "@/components/ui/button";
import { Card } from "@/components/ui/card";
import { toast } from "sonner";

interface UploadedFile {
  id: string;
  name: string;
  size: number;
}

export const FileUpload = () => {
  const [files, setFiles] = useState<UploadedFile[]>([]);
  const [isDragging, setIsDragging] = useState(false);
  const [uploading, setUploading] = useState(false);

  const uploadFile = async (file: File) => {
    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await fetch("http://localhost:5000/upload", {
        method: "POST",
        body: formData,
      });

      if (!response.ok) {
        throw new Error("Upload failed");
      }

      return {
        id: Math.random().toString(36).substr(2, 9),
        name: file.name,
        size: file.size,
      };
    } catch (error) {
      console.error("Upload error:", error);
      throw error;
    }
  };

  const handleFiles = useCallback(async (fileList: FileList) => {
    setUploading(true);
    const uploadPromises = Array.from(fileList).map(async (file) => {
      try {
        const uploadedFile = await uploadFile(file);
        toast.success(`${file.name} uploaded successfully`);
        return uploadedFile;
      } catch (error) {
        toast.error(`Failed to upload ${file.name}`);
        return null;
      }
    });

    const results = await Promise.all(uploadPromises);
    const successfulUploads = results.filter((f): f is UploadedFile => f !== null);
    setFiles((prev) => [...prev, ...successfulUploads]);
    setUploading(false);
  }, []);

  const handleDrop = useCallback(
    (e: React.DragEvent) => {
      e.preventDefault();
      setIsDragging(false);
      if (e.dataTransfer.files) {
        handleFiles(e.dataTransfer.files);
      }
    },
    [handleFiles]
  );

  const handleDragOver = useCallback((e: React.DragEvent) => {
    e.preventDefault();
    setIsDragging(true);
  }, []);

  const handleDragLeave = useCallback(() => {
    setIsDragging(false);
  }, []);

  const handleFileInput = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files) {
      handleFiles(e.target.files);
    }
  };

  const removeFile = (id: string) => {
    setFiles((prev) => prev.filter((f) => f.id !== id));
    toast.info("File removed from list");
  };

  const formatFileSize = (bytes: number) => {
    if (bytes < 1024) return bytes + " B";
    if (bytes < 1024 * 1024) return (bytes / 1024).toFixed(1) + " KB";
    return (bytes / (1024 * 1024)).toFixed(1) + " MB";
  };

  return (
    <div className="flex flex-col h-full gap-4">
      <div
        className={`relative border-2 border-dashed rounded-xl p-8 transition-all ${
          isDragging
            ? "border-primary bg-primary/5 scale-[1.02]"
            : "border-border bg-card hover:border-primary/50"
        }`}
        onDrop={handleDrop}
        onDragOver={handleDragOver}
        onDragLeave={handleDragLeave}
      >
        <input
          type="file"
          id="file-upload"
          className="hidden"
          multiple
          onChange={handleFileInput}
          disabled={uploading}
        />
        <label
          htmlFor="file-upload"
          className="flex flex-col items-center justify-center cursor-pointer"
        >
          {uploading ? (
            <Loader2 className="w-12 h-12 text-primary animate-spin mb-4" />
          ) : (
            <Upload className="w-12 h-12 text-primary mb-4" />
          )}
          <p className="text-lg font-medium text-foreground mb-1">
            {uploading ? "Uploading..." : "Drop files here or click to upload"}
          </p>
          <p className="text-sm text-muted-foreground">
            PDF, TXT, DOC, and more supported
          </p>
        </label>
      </div>

      <div className="flex-1 overflow-y-auto space-y-2">
        {files.length === 0 ? (
          <Card className="p-8 text-center">
            <File className="w-12 h-12 text-muted-foreground mx-auto mb-2" />
            <p className="text-muted-foreground">No files uploaded yet</p>
          </Card>
        ) : (
          files.map((file) => (
            <Card
              key={file.id}
              className="p-4 flex items-center justify-between hover:shadow-md transition-shadow"
            >
              <div className="flex items-center gap-3">
                <div className="w-10 h-10 rounded-lg bg-primary/10 flex items-center justify-center">
                  <File className="w-5 h-5 text-primary" />
                </div>
                <div>
                  <p className="font-medium text-foreground">{file.name}</p>
                  <p className="text-sm text-muted-foreground">
                    {formatFileSize(file.size)}
                  </p>
                </div>
              </div>
              <Button
                variant="ghost"
                size="icon"
                onClick={() => removeFile(file.id)}
                className="hover:bg-destructive/10 hover:text-destructive"
              >
                <X className="w-4 h-4" />
              </Button>
            </Card>
          ))
        )}
      </div>
    </div>
  );
};
