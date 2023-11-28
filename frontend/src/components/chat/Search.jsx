import React, { useState } from 'react';


const Search = ({ onButtonClick, setSearchValue, isGetSuccess, foundedUser, isGetError }) => {
    const [inputValue, setInputValue] = useState('');

    const onSubmitForm = (e) => {
        e.preventDefault();
        setSearchValue(inputValue);
    }

    return (
        <div className='search'>
            <form className='search-form' onSubmit={onSubmitForm}>
                <input 
                    placeholder='Find a user' 
                    value={inputValue} 
                    onChange={e => setInputValue(e.target.value)}>
                </input>
                <button>Search</button>
            </form>
            {isGetSuccess ? 
            <div className='user-chat'>
                <img src='https://images.pexels.com/photos/18983851/pexels-photo-18983851.jpeg?auto=compress&cs=tinysrgb&w=400&lazy=load' alt=''></img>
                <div className='user-chat-info'>
                    <span>{foundedUser.username}</span>
                    <button onClick={onButtonClick}>+</button>
                </div>
            </div>
            : isGetError ?
            <div className='not-found'>
                <span>User not found</span>
            </div>
            :
            null
            }
        </div>
    )
}

export default Search;
