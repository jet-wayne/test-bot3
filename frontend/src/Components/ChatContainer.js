// src/components/ChatContainer.jsx
import React, { useEffect, useRef } from "react";
import ChatBubble from "./ChatBubble";

const ChatContainer = ({ messages }) => {
  const containerRef = useRef(null);

  useEffect(() => {
    containerRef.current?.scrollTo(0, containerRef.current.scrollHeight);
  }, [messages]);

  return (
    <div ref={containerRef} className="flex-grow p-4 overflow-y-auto">
      {messages.map((msg, index) => (
        <ChatBubble key={index} message={msg.text} sender={msg.sender} />
      ))}
    </div>
  );
};

export default ChatContainer;
