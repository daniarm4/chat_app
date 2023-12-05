import { BrowserRouter, Routes, Route } from 'react-router-dom';
import React from 'react';
import { useSelector } from 'react-redux';
import ChatPage from './pages/chatpage/ChatPage';
import Loading from './components/loading/Loading';
import { useCheckAuthQuery } from './store/api/userApi';
import AuthPage from './pages/AuthPage';
import Login from './components/auth/login/Login';
import Register from './components/auth/register/Register';


const App = () => {
    const { isLoading } = useCheckAuthQuery();
    const { isAuth } = useSelector(state => state.user)
    if (isLoading) {
        return <Loading />;
    }
    
    return (
        <BrowserRouter>
            <Routes>
                <Route path='/' element={<AuthPage />}>
                    <Route path='/login' element={<Login />} />
                    <Route path='/register' element={<Register />} />
                </Route>
                {isAuth ?
                <Route path='/chats' element={<ChatPage />} /> :
                null}
            </Routes>
        </BrowserRouter>
    )
}

export default App;
