import React from 'react';
import { Link } from 'react-router-dom';
import LoginForm from './LoginForm';

const Login = () => {
    return (
        <>
            <span className='title'>Chat</span>
            <span className='subtitle'>Login</span>
            <LoginForm />
            <p>Don't have an account? <Link to='/register'>Register</Link></p>
        </>
    )
}

export default Login;