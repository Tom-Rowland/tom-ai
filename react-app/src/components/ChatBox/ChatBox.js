// ChatBox.js
import React from 'react';
import './ChatBox.css';

const UserMessage = ({ message }) => {
  return (
    <div className="user-message text-right">
      {message}
    </div>
  );
};

const BotMessage = ({ message }) => {
  return (
    <div className="bot-message">
      {message}
    </div>
  );
};

const ChatBox = ({ message, isUser }) => {
  return isUser ? <UserMessage message={message} /> : <BotMessage message={message} />;
};

export default ChatBox;
