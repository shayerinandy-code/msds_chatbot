import React, { useEffect, useRef, useState } from "react";
import { ChatMessage } from "../types";
import { postQuery } from "../api";
import "./ChatView.css";

interface Props {
  conversations: ChatMessage[][];
  selectedConversation: number | null;
  setConversations: React.Dispatch<React.SetStateAction<ChatMessage[][]>>;
}

const ChatView: React.FC<Props> = ({
  conversations,
  selectedConversation,
  setConversations,
}) => {
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);
  const [strict, setStrict] = useState(false);

  const bottomRef = useRef<HTMLDivElement | null>(null);

  const messages =
    selectedConversation !== null
      ? conversations[selectedConversation] || []
      : [];

  // ✅ Auto-scroll like ChatGPT
  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [conversations, selectedConversation]);

  

  const sendMessage = async () => {
  if (!input.trim() || loading) return;

  let convoIndex = selectedConversation;

  // ✅ Auto-create conversation if none selected
  if (convoIndex === null) {
    setConversations(prev => [...prev, []]);
    convoIndex = conversations.length;
  }

  const userMsg: ChatMessage = {
    id: crypto.randomUUID(),
    role: "user",
    content: input,
    createdAt: new Date().toISOString(),
  };

  setConversations(prev => {
    const next = [...prev];
    next[convoIndex!] = [...(next[convoIndex!] || []), userMsg];
    return next;
  });

  setInput("");
  setLoading(true);

  try {
    const res = await postQuery(input, 5, strict);

    const botMsg: ChatMessage = {
      id: crypto.randomUUID(),
      role: "assistant",
      content: res.answer || "No answer found",
      createdAt: new Date().toISOString(),
    };

    setConversations(prev => {
      const next = [...prev];
      next[convoIndex!] = [...next[convoIndex!], botMsg];
      return next;
    });
  } finally {
    setLoading(false);
  }
};

  return (
    <div className="chat-root">
      <div className="chat-messages">
        {messages.map(m => (
          <div key={m.id} className={`bubble ${m.role}`}>
            {m.content}
          </div>
        ))}
        <div ref={bottomRef} />
      </div>

      <div className="chat-input-wrapper">
        <label className="strict">
          <input
            type="checkbox"
            checked={strict}
            onChange={e => setStrict(e.target.checked)}
          />
          STRICT
        </label>

        <div className="chat-input-box">
          <input
            value={input}
            onChange={e => setInput(e.target.value)}
            onKeyDown={e => e.key === "Enter" && sendMessage()}
            placeholder="Ask about SDS (e.g. First aid measures)"
          />
          <button onClick={sendMessage} disabled={loading}>
            Send
          </button>
        </div>
      </div>
    </div>
  );
};

export default ChatView;
