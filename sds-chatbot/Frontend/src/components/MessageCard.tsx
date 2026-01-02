import React from "react";
import { ChatMessage } from "../types";

interface Props {
  msg: ChatMessage;
}

const MessageCard: React.FC<Props> = ({ msg }) => {
  return (
    <div className={`message ${msg.role}`}>
      <p>{msg.content}</p>

      {/* ✅ EXACT SDS PARAGRAPH */}
      {msg.highlightedText && (
        <details>
          <summary>🔍 View exact SDS paragraph</summary>
          <pre>{msg.highlightedText}</pre>
        </details>
      )}

      {/* ✅ SOURCE */}
      {msg.source && (
        <div className="source">
          📄 <strong>Source:</strong> {msg.source}
        </div>
      )}

      {/* ✅ CONFIDENCE */}
      {msg.confidence && (
        <div className="confidence">
          🔎 Confidence: {msg.confidence}/10
        </div>
      )}
    </div>
  );
};

export default MessageCard;
