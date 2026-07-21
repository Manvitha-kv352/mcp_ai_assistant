function Message({ role, text }) {
  const isUser = role === 'user'

  return (
    <div className={`message ${isUser ? 'user' : 'assistant'}`}>
      <div className="message-bubble">
        {text}
      </div>
    </div>
  )
}

export default Message
