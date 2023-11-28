import ChatPage from './pages/ChatPage';
import RegisterPage from './pages/RegisterPage';
import LoginPage from './pages/LoginPage';
import NotFoundPage from './pages/NotFoundPage';

export const protectedRoutes = [
    {path: '/chats', element: <ChatPage />}
]

export const defaultRoutes = [
    {path: '/register', element: <RegisterPage />},
    {path: '/login', element: <LoginPage />},
    {path: '*', element: <NotFoundPage />}
]
