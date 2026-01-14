"use client";

import { useState } from "react";

export default function Chat() {
  const [messages, setMessages] = useState<{ role: string; content: string }[]>(
    []
  );
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);

  async function sendMessage() {
    if (!input.trim()) return;

    // Dodaj korisnikovu poruku
    const userMessage = { role: "user", content: input };
    setMessages((prev) => [...prev, userMessage]);
    setInput("");

    setLoading(true);

    // Pošalji backendu
    const res = await fetch("http://localhost:8000/api/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: userMessage.content }), // OVO backend očekuje
    });

    const data = await res.json();

    setLoading(false);

    // Dodaj botov odgovor
    const botMessage = { role: "assistant", content: data.answer };
    setMessages((prev) => [...prev, botMessage]);
  }

  return (
    <div className="max-w-xl mx-auto py-10">
      <div className="border rounded-lg p-4 h-500px overflow-y-auto bg-white shadow">
        {messages.map((msg, i) => (
          <div
            key={i}
            className={`mb-3 p-2 rounded ${
              msg.role === "user"
                ? "bg-blue-100 text-blue-900"
                : "bg-gray-100 text-gray-900"
            }`}
          >
            {msg.content}
          </div>
        ))}

        {loading && (
          <div className="mb-3 p-2 rounded bg-gray-100 text-gray-500 w-fit animate-pulse">
            Thinking...
          </div>
        )}
      </div>

      <div className="flex gap-2 mt-4">
        <input
          className="flex-1 border rounded p-2"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Upiši poruku…"
        />
        <button
          onClick={sendMessage}
          className="bg-blue-600 text-white px-4 py-2 rounded cursor-pointer"
        >
          Send
        </button>
      </div>
    </div>
  );
}
