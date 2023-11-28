import React from 'react';
import { Link } from 'react-router-dom';
import './auth.css'
import LoginForm from './LoginForm';

const Login = () => {
    return (
        <div className='form-container'>
            <div className='form-wrapper'>
                <span className='title'>Chat</span>
                <span className='subtitle'>Login</span>
                <LoginForm />
                <p>Don't have an account? <Link to='/register'>Register</Link></p>
            </div>
        </div>
    )
}

export default Login;