import React, { useState } from 'react';
import { useDispatch } from 'react-redux';
import { setChat } from '../../store/reducers/chatSlice';
import { useGetChatsByUserIdQuery } from '../../store/api/chatApi';
import Loading from '../loading/Loading'


const ChatList = () => {
    const dispatch = useDispatch();
    const { data: chats, isLoading, isSuccess, isError } = useGetChatsByUserIdQuery();

    const chatOnClick = (chatId, chatName) => {
        dispatch(setChat({chatId: chatId, chatName: chatName}));
    }

    if (isLoading) {
        return <Loading />
    }
    
    return (
        <>
            {chats.chats.map(chat => {
                return (
                    <div className='chat-list' 
                        id={chat[1]} 
                        onClick={() => chatOnClick(chat[1], chat[0])}>
                        <div className='user-chat hover-user-chat'>
                            <img src='https://images.pexels.com/photos/18983851/pexels-photo-18983851.jpeg?auto=compress&cs=tinysrgb&w=400&lazy=load' alt=''></img>
                            <div className='user-chat-info'>
                                <span>{chat[0]}</span>
                            </div>
                        </div>
                    </div>
                )
            })}
        </>
    )
}

export default ChatList;
