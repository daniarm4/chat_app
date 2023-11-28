import React from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { userLogout } from '../../store/reducers/userSlice';


const ChatNavbar = () => {
    const dispatch = useDispatch();
    const { username } = useSelector(state => state.user);

    const handleLogoutButtonClick = () => {
        dispatch(userLogout());
        localStorage.clear();
    }

    return (
        <div className='chat-navbar'>
            <span className='logo'>Chat</span>
            <div className='user'>
                <img src='https://images.pexels.com/photos/18983851/pexels-photo-18983851.jpeg?auto=compress&cs=tinysrgb&w=400&lazy=load' alt=''></img>
                <span>{username}</span>
                <button onClick={handleLogoutButtonClick}>logout</button>
            </div>
        </div>
    )
}

export default ChatNavbar;
