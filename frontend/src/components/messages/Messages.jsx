import React, { useLayoutEffect, useRef } from "react";
import Message from "./Message";
import './messages.css'

const Messages = ({messages}) => {
    const messageBox = useRef(null);
    useLayoutEffect(() => {
        if (messageBox) {
            messageBox.current.scrollTop = messageBox.current.scrollHeight;
        }
    }, [messages])

    return (
        <div className="messages" ref={messageBox}>
            {messages.map(message => 
                <Message message={message} key={message.id} />
            )}
        </div>
    )
}

export default Messages;
