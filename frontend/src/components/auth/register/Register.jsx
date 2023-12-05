import React from 'react';
import { Link } from 'react-router-dom';
import RegisterForm from './RegisterForm';


const Register = () => {
    return (
        <>
            <span className='title'>Chat</span>
            <span className='subtitle'>Register</span>
            <RegisterForm />
            <p>Already have an account? <Link to='/login'>Login</Link></p>
        </>
    )
}

export default Register;
