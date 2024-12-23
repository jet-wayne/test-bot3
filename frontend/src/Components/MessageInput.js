// src/components/MessageInput.jsx
import React, { useState } from "react";

const MessageInput = ({ onSend }) => {
  const [message, setMessage] = useState("");

  const handleSend = () => {
    if (message.trim()) {
      onSend(message);
      setMessage("");
    }
  };

  const handleKeyPress = (e) => {
    if (e.key === "Enter") {
      handleSend();
    }
  };

  return (
    <div className="flex items-center p-2 border-t border-gray-300">
      <input
        type="text"
        className="flex-grow p-2 border rounded-lg focus:outline-none"
        placeholder="Type your message..."
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        onKeyPress={handleKeyPress}
      />
      <button
        className="ml-2 p-2 bg-[#1BD760] text-zinc-800 rounded-lg"
        onClick={handleSend}>
        Send
      </button>
    </div>
  );
};

export default MessageInput;
