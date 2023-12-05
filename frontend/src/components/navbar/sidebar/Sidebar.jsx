import { useDispatch } from 'react-redux';
import { userLogout } from '../../../store/reducers/userSlice'
import './sidebar.scss';


const Sidebar = () => {
    const dispatch = useDispatch();

    const handleLogoutClick = () => {
        dispatch(userLogout());
        localStorage.clear();
    }

    return (
        <div className="sidebar">
            <div className='links'>
                <img className='sidebar-icon active' src='https://img.icons8.com/?size=50&id=118377&format=png' />
                <img className='sidebar-icon' src='https://img.icons8.com/?size=50&id=11642&format=png' />
                <img 
                    className='sidebar-icon' 
                    src='https://img.icons8.com/?size=50&id=2445&format=png' 
                    onClick={handleLogoutClick} 
                />
            </div>
            <div className='user-avatar'>
                <img className="avatar" src='https://img2.freepng.ru/20180430/jww/kisspng-google-account-google-analytics-google-search-cons-5ae6b1e5dbec48.6537645315250682619008.jpg' />
                <span className='avatar-circle'></span>
            </div>
        </div>
    )
}

export default Sidebar;
