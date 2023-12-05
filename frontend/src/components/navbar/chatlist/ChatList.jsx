import React from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { setChat } from '../../../store/reducers/chatSlice';
import { useGetChatsByUserIdQuery } from '../../../store/api/chatApi';
import Loading from '../../loading/Loading';
import './chatlist.scss';

const ChatList = () => {
    const dispatch = useDispatch();
    const selectedChatId = useSelector(state => state.chat.chatId)
    const { data: chats, isLoading, isSuccess, isError } = useGetChatsByUserIdQuery();

    const chatOnClick = (chatId, chatName) => {
        dispatch(setChat({chatId: chatId, chatName: chatName}));
    }

    if (isLoading) {
        return <Loading />
    }
    
    return (
        <div className='chat-list-container'>
            <span className='chat-list-title'>Chat list</span>
            <div className='chat-list'>
            {chats.chats.map(chat => {
                return (
                    <div 
                    className={selectedChatId === chat[0] ? 'chat-list-item active' : 'chat-list-item'}
                    id={chat[1]} 
                    onClick={() => chatOnClick(chat[1], chat[0])}>
                        <div className='user-avatar'>
                            <img className="avatar" src='https://img2.freepng.ru/20180430/jww/kisspng-google-account-google-analytics-google-search-cons-5ae6b1e5dbec48.6537645315250682619008.jpg' />
                            <span className='avatar-circle'></span>
                        </div>
                        <div className='chat-content'>
                            <span className="chat-title">{chat[0]}</span>
                            <span className="chat-subtitle">Hello john</span>
                        </div>
                    </div>
                )
            })}
            </div>
        </div>
    )
}

export default ChatList;
