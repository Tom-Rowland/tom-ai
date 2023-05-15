// ChatContainer.js
import React, { useState } from 'react';
import ChatBox from '../ChatBox/ChatBox.js';
import TextBox from '../TextBox/TextBox.js';

const ChatContainer = () => {
  const [messages, setMessages] = useState([]);

  const sendMessage = (message) => {
    setMessages((prevMessages) => [
      ...prevMessages,
      { text: message, isUser: true },
      { text: "I am a bot", isUser: false },
    ]);
  };
  

  return (
    <div className="chat-container">
      <div className="chat-messages">
        {messages.map((message, index) => (
          <ChatBox
            key={index}
            message={message.text}
            isUser={message.isUser}
          />
        ))}
      </div>
      <TextBox onSendMessage={sendMessage} />
    </div>
  );
};

export default ChatContainer;
