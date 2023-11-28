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
        <div className='message-input'>
            <input 
                type='text' 
                placeholder='Type message' 
                value={message} 
                onKeyDown={onKeyDown}
                onChange={e => setMessage(e.target.value)}>
            </input>
            <button className='send-button' onClick={handleClick}>Send message</button>
        </div>
    )
}

export default Input;
