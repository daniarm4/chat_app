import React from 'react';
import { Link } from 'react-router-dom';
import './auth.css'
import RegisterForm from './RegisterForm';


const Register = () => {
    return (
        <div className='form-container'>
            <div className='form-wrapper'>
                <span className='title'>Chat</span>
                <span className='subtitle'>Register</span>
                <RegisterForm />
                <p>Already have an account? <Link to='/login'>Login</Link></p>
            </div>
        </div>
    )
}

export default Register;
