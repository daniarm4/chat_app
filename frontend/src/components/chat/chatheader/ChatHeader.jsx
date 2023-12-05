import { useSelector } from 'react-redux';
import './chatheader.scss';

const ChatHeader = () => {
    const chatName = useSelector(state => state.chat.chatName);

    return (
      <div className='header'>
          <div className="header-info">
              <div className='user-avatar'>
                  <img className="avatar" src='https://shapka-youtube.ru/wp-content/uploads/2020/12/man-ava1.jpg'></img>
                  <span className='avatar-circle'></span>
              </div>
              <span className="username">{chatName}</span>
          </div>
          <img className="chat-options" src='https://img.icons8.com/?size=50&id=36944&format=png' />
      </div>  
    )
}

export default ChatHeader