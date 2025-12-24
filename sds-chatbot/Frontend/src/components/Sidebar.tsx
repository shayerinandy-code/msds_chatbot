import React from "react";
import { ChatMessage } from "../types";
import "./Sidebar.css";

interface Props {
  conversations: ChatMessage[][];
  selectedConversation: number | null;
  onSelect: (index: number) => void;
  onNew: () => void;
  onDelete: (index: number) => void;
}

const Sidebar: React.FC<Props> = ({
  conversations,
  selectedConversation,
  onSelect,
  onNew,
  onDelete,
}) => {
  return (
    <aside className="sidebar">
      <h2>SDS Chatbot</h2>

      <button className="new-chat" onClick={onNew}>
        + New Chat
      </button>

      <div className="chat-list">
        {conversations.map((_, i) => (
          <div
            key={i}
            className={`chat-item ${
              selectedConversation === i ? "active" : ""
            }`}
            onClick={() => onSelect(i)}
          >
            <span>Conversation {i + 1}</span>
            <button
              className="delete"
              onClick={(e) => {
                e.stopPropagation();
                onDelete(i);
              }}
            >
              ✕
            </button>
          </div>
        ))}
      </div>
    </aside>
  );
};

export default Sidebar;
