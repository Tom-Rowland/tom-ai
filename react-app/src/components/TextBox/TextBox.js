// TextBox.js
// TextBox.js
import React, { useState } from 'react';
import './TextBox.css';

const TextBox = ({ onSendMessage }) => {
  const [input, setInput] = useState('');

  const handleInputChange = (e) => {
    setInput(e.target.value);
  };

  const handleKeyPress = (e) => {
    if (e.key === 'Enter') {
      onSendMessage(input);
      setInput('');
    }
  };

  return (
    <div className="textbox">
      <input
        type="text"
        placeholder="Type your message..."
        value={input}
        onChange={handleInputChange}
        onKeyPress={handleKeyPress}
      />
    </div>
  );
};

export default TextBox;

