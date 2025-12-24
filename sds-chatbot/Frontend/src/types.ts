export interface TopMatch {
  snippet: string;
  source: string;
  distance?: number;
}

export interface ChatMessage {
  id: string;
  role: "user" | "assistant";
  content: string;
  createdAt: string;

  source_file?: string;
  section?: string;
  context_used?: string[] | string;
  top_matches?: TopMatch[];
}
