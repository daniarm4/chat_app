import ChatList from './chatlist/ChatList'
import Sidebar from './sidebar/Sidebar'
import './navbar.scss'

const Navbar = () => {
    return (
        <nav>
            <Sidebar />
            <ChatList />
        </nav>
    )
}

export default Navbar