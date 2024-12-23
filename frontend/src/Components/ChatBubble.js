// src/components/ChatBubble.jsx
import React from "react";

const ChatBubble = ({ message, sender }) => {
  const isUser = sender === "user";
  return (
    <div className={`flex ${isUser ? "justify-start" : "justify-end"} mb-4`}>
      <div
        className={`max-w-xs px-4 py-2 rounded-lg ${
          isUser ? "bg-[#1BD760] text-zinc-800" : "bg-gray-300 text-gray-800"
        } ${isUser ? "rounded-bl-none" : "rounded-br-none"}`}>
        {message}
      </div>
    </div>
  );
};

export default ChatBubble;
