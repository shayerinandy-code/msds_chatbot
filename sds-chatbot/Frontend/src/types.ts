export interface ChatMessage {
  role: "user" | "assistant";
  content: string;
  confidence?: number;
  source?: string;
  highlightedText?: string;
}
