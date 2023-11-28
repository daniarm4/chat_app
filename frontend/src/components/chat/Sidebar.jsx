import React, { useState } from 'react';
import ChatNavbar from './ChatNavbar';
import Search from './Search';
import ChatList from './ChatList';
import { useSelector } from 'react-redux';
import { useGetUserQuery } from '../../store/api/userApi';
import { useCreateChatMutation } from '../../store/api/chatApi';

const Sidebar = () => {
    const currentUser = useSelector(state => state.user.username);
    const [ searchValue, setSearchValue ] = useState('');

    const { 
        data: foundedUser, 
        isLoading: isGetLoading, 
        isError: isGetError, 
        isSuccess: isGetSuccess
    } = useGetUserQuery(searchValue, {
            refetchOnMountOrArgChange: true,
            skip: !searchValue
        });

    const [createChat] = useCreateChatMutation();

    const onButtonClick = () => {
        if (isGetSuccess) {
            createChat({users_username: [currentUser, foundedUser.username]});
        }
    }

    return (
        <div className='sidebar'>
            <ChatNavbar />
            <Search 
                setSearchValue={setSearchValue}
                onButtonClick={onButtonClick}
                isGetSuccess={isGetSuccess}
                foundedUser={foundedUser} 
                isGetError={isGetError}/>
            <ChatList />
        </div>
    )
}

export default Sidebar;
