import React, { useState } from "react";
import "./styles.css";

type Message = {
  role: "user" | "assistant";
  content: string;
};

export default function App() {
  const [messages, setMessages] = useState<Message[]>([
    { role: "assistant", content: "Hi! Ask me anything about SDS." },
  ]);
  const [input, setInput] = useState("");

  const sendMessage = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!input.trim()) return;

    const userMessage: Message = { role: "user", content: input };
    setMessages((prev) => [...prev, userMessage]);
    setInput("");

    const res = await fetch("http://localhost:8000/api/v1/query", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        query: input,
        product: "ESPL-30-Seconds-Nzl-En-090625-1",
      }),
    });

    const data = await res.json();

    setMessages((prev) => [
      ...prev,
      { role: "assistant", content: data.answer },
    ]);
  };

  const startNewChat = () => {
    setMessages([{ role: "assistant", content: "Hi! Ask me anything about SDS." }]);
  };

  return (
    <div className="app">
      <aside className="sidebar">
        <h2>SDS Chatbot</h2>
        <button onClick={startNewChat}>+ New Chat</button>
      </aside>

      <main className="chat">
        <div className="messages">
          {messages.map((msg, i) => (
            <div
              key={i}
              className={`message ${msg.role === "user" ? "user" : "bot"}`}
            >
              {msg.content}
            </div>
          ))}
        </div>

        <form className="input-bar" onSubmit={sendMessage}>
          <button type="button" className="plus">+</button>
          <input
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder="Ask anything"
          />
          <button type="submit">Send</button>
        </form>
      </main>
    </div>
  );
}
