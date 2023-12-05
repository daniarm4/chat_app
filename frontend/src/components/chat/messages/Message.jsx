import { useSelector } from "react-redux";
import './message.scss';

const Message = ({message}) => {
    const { userId, username } = useSelector(state => state.user);
    const chatName = useSelector(state => state.chat.chatName);
    const isOwner = Boolean(userId === message.sender_id);
    const sender = isOwner ? username : chatName;
    const messageCreated = new Date(message.created_at);
    const hours = messageCreated.getHours().toString().length < 2 ? '0' + messageCreated.getHours() : messageCreated.getHours();
    const minutes = messageCreated.getMinutes().toString().length < 2 ? '0' + messageCreated.getMinutes() : messageCreated.getMinutes();

    return (
        <div className={!isOwner ? 'message' : 'message owner'}>
            <div className='user-avatar'>
                <img className="avatar" src='https://shapka-youtube.ru/wp-content/uploads/2020/12/man-ava1.jpg'></img>
                <span className='avatar-circle'></span>
            </div>
            <div className="message-content">
                <div className="message-info">
                    <div className="message-sender">{sender}</div>
                    <div className="message-created">{`${hours}:${minutes}`}</div>
                </div>
                <div className={!isOwner ? "message-text" : "message-text message-text-owner"}>{message.text}</div>
            </div>
        </div>
    )
}

export default Message;
