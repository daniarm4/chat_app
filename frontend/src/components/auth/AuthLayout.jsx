import './auth.scss';
import { Outlet } from "react-router-dom";

const AuthLayout = () => {
    return (
        <div className='form-container'>
            <div className='form-wrapper'>
                <Outlet />
            </div>
        </div>
    )
}

export default AuthLayout;