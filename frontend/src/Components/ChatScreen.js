// src/screens/ChatScreen.jsx
import React, { useState } from "react";
import ChatContainer from "./ChatContainer";
import MessageInput from "./MessageInput";

const ChatScreen = () => {
  const [messages, setMessages] = useState([]);

  const handleSendMessage = async (text) => {
    const newMessage = { text, sender: "user" };
    setMessages((prev) => [...prev, newMessage]);

    // Simulating API call
    const response = await fetch(
      "https://starhub-faq-search-ohycf5coga-as.a.run.app/api/chat",
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          query: text,
        }),
      }
    );

    const data = await response.json();
    const botMessage = { text: data.response, sender: "bot" };
    setMessages((prev) => [...prev, botMessage]);
  };

  return (
    <div className="flex justify-center items-center h-screen bg-slate-400">
      <div className="w-full lg:w-4/12 h-[calc(100%-8px)] my-[4px] border border-gray-300 rounded-lg flex flex-col bg-white">
        <div className="bg-[#1BD760] w-full  text-zinc-800 p-4 text-center font-semibold rounded-lg">
          StarHub Bot
        </div>
        <ChatContainer messages={messages} />
        <MessageInput onSend={handleSendMessage} />
      </div>
    </div>
  );
};

export default ChatScreen;
