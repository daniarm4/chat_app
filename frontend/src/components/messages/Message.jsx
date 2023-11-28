import React from "react";
import { useSelector } from "react-redux";


const Message = ({message}) => {
    const userId = useSelector(state => state.user.userId);
    const isOwner = Boolean(userId === message.sender_id);
    return (
        <div className={!isOwner ? 'message' : 'message message-owner'}>
            <div className="message-info">
                <img src='https://images.pexels.com/photos/18983851/pexels-photo-18983851.jpeg?auto=compress&cs=tinysrgb&w=400&lazy=load' alt=''></img>
            </div>
            <div className={!isOwner ? 'message-content' : 'message-content message-content-owner'}>
                <p>{message.text}</p>
                <span>{message.created_at}</span>
            </div>
        </div>
    )
}

export default Message;
