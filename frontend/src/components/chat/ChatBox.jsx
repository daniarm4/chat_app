import React from 'react';
import Messages from '../messages/Messages';
import Input from './Input';
import useWebSocket from 'react-use-websocket';
import { useDispatch, useSelector } from 'react-redux';
import { useGetMessagesQuery } from '../../store/api/chatApi';
import { api } from '../../store/api/base';

const ChatBox = () => {
    const state = useSelector(state => state);
    const dispatch = useDispatch();
    const { userId } = state.user;
    const { chatName, chatId } = state.chat;
    const wsUrl = `ws://localhost:8000/chats/ws/${chatId}`;
    const { data: messages, isLoading } = useGetMessagesQuery(chatId, {
        skip: !chatId
    });

    const { sendJsonMessage } = useWebSocket(wsUrl, {
        onMessage: (event) => {
            let data = JSON.parse(event.data);
            dispatch(
                api.util.updateQueryData('getMessages', chatId, (draft) => {
                    draft.messages.push(data['message']);
                })
            )
        }
    }); 

    const addNewMessage = (message) => {
        const messageData = {'text': message, 'sender_id': userId, 'chat_id': chatId};
        sendJsonMessage({'message': messageData});
    }

    if (isLoading || !chatId) {
        return (
            <div className='chat-box'>
                <div className='chat-info'>
                    <span>Chat not selected</span>
                </div>
            </div>
        )
    }

    return (
        <div className='chat-box'>
            <div className='chat-info'>
                <span>{chatName}</span>
            </div>
            <Messages messages={messages.messages} />
            <Input addMessage={(message) => addNewMessage(message)} />
        </div>
    )
}

export default ChatBox;
