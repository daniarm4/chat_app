import React from 'react';
import { Link } from 'react-router-dom';
import './nav.css'

const Navbar = () => {
    return (
        <header>
            <nav className='navigation'>
                <Link to='/register'>Register</Link>
                <Link to='/login'>Login</Link>
            </nav>
        </header>
    )
}

export default Navbar;
