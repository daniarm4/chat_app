import ChatBox from '../../components/chat/chatbox/ChatBox'
import ChatHeader from '../../components/chat/chatheader/ChatHeader'
import Navbar from '../../components/navbar/Navbar'
import './chatpage.scss'

const Chat = () => {
  return (
    <div className='container'>
        <Navbar />
        <main>
            <ChatHeader />
            <ChatBox />
        </main>
    </div>
  )
}

export default Chat