// src/components/MessageCard.tsx
import React from "react";
import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
import { ChatMessage } from "../types";
import "./MessageCard.css";

interface Props {
  msg: ChatMessage;
}

const MessageCard: React.FC<Props> = ({ msg }) => {
  return (
    <div className={`msg ${msg.role === "user" ? "user" : "bot"}`}>
      {msg.role === "assistant" ? (
        <ReactMarkdown remarkPlugins={[remarkGfm]}>
          {msg.content}
        </ReactMarkdown>
      ) : (
        <span>{msg.content}</span>
      )}

      {msg.source_file && (
        <div className="msg-source">
          📄 {msg.source_file}
          {msg.section && ` · Section ${msg.section}`}
        </div>
      )}
    </div>
  );
};

export default MessageCard;
