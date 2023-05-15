// ChatContainer.js
import React, { useState } from 'react';
import ChatBox from '../ChatBox/ChatBox.js';
import TextBox from '../TextBox/TextBox.js';

const ChatContainer = () => {
  const [messages, setMessages] = useState([]);

  const sendMessage = (message) => {
    // Handle the message and update the conversation
    // You can add your logic here to interact with the backend or process the message

    // For example, appending the user's message to the conversation
    setMessages([...messages, { text: message, isUser: true }]);
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
