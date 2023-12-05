import './input.scss';
import React, { useState } from 'react';


const Input = ({addMessage}) => {
    const [message, setMessage] = useState('');

    const handleClick = () => {
        addMessage(message);
        setMessage('');
    }

    const onKeyDown = (event) => {
        if (event.key === 'Enter') {
            handleClick();
        }
    }

    return (
        <div className="chat-input">
            <input 
                type='text' 
                placeholder='Type message' 
                value={message} 
                onKeyDown={onKeyDown}
                onChange={e => setMessage(e.target.value)}>
            </input>
            <button onClick={handleClick}><img src='send-message.png'/></button>
        </div>
    )
}

export default Input;
