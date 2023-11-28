import React from 'react';
import ChatBox from '../components/chat/ChatBox';
import Sidebar from '../components/chat/Sidebar';
import '../components/chat/chat.css'


const ChatPage = () => {
    return (
        <div className='chat-container'>
            <div className='chat-wrapper'>
                <Sidebar />
                <ChatBox />
            </div>
        </div>
    )
}

export default ChatPage;
