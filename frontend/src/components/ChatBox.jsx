import { useState, useEffect, useRef } from 'react'
import Message from './Message'
import { sendMessage, uploadFile } from '../services/api'

function ChatBox() {
  const [messages, setMessages] = useState([
    { role: 'assistant', text: 'Hello! I can help with documents, API calls, databases, and files.' },
  ])
  const [input, setInput] = useState('')
  const [loading, setLoading] = useState(false)
  const [sessionId, setSessionId] = useState(() => localStorage.getItem('mcp-session-id') || '')
  const [uploading, setUploading] = useState(false)
  const [activeFile, setActiveFile] = useState('')
  const bottomRef = useRef(null)

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: 'smooth' })
  }, [messages, loading])

  useEffect(() => {
    if (!sessionId) {
      const freshSession = `session-${Date.now()}`
      localStorage.setItem('mcp-session-id', freshSession)
      setSessionId(freshSession)
    }
  }, [sessionId])

  const handleSubmit = async (e) => {
    e.preventDefault()
    const trimmed = input.trim()
    if (!trimmed) return

    const userMessage = { role: 'user', text: trimmed }
    setMessages((prev) => [...prev, userMessage])
    setInput('')
    setLoading(true)

    try {
      const response = await sendMessage(trimmed, sessionId || 'demo-session')
      const reply = typeof response === 'string'
        ? response
        : response?.response || response?.message || 'No response received.'
      setMessages((prev) => [...prev, { role: 'assistant', text: reply }])
    } catch (err) {
      setMessages((prev) => [...prev, { role: 'assistant', text: 'The backend is unavailable right now. Please make sure the FastAPI server is running.' }])
    } finally {
      setLoading(false)
    }
  }

  const handleFileUpload = async (e) => {
    const file = e.target.files?.[0]
    if (!file) return

    setUploading(true)
    try {
      const result = await uploadFile(file, sessionId || 'demo-session')
      setActiveFile(result.filename || file.name)
      setMessages((prev) => [...prev, { role: 'assistant', text: `Uploaded ${result.filename || file.name} and indexed it for this chat session.` }])
    } catch (err) {
      setMessages((prev) => [...prev, { role: 'assistant', text: 'Upload failed. Please try again.' }])
    } finally {
      setUploading(false)
      e.target.value = ''
    }
  }

  const startNewChat = () => {
    const freshSession = `session-${Date.now()}`
    localStorage.setItem('mcp-session-id', freshSession)
    setSessionId(freshSession)
    setActiveFile('')
    setMessages([{ role: 'assistant', text: 'New chat started. You can upload a file or ask a question.' }])
  }

  return (
    <div className="chat-card">
      <div className="chat-toolbar">
        <span className="session-pill">Session: {sessionId || 'new'}</span>
        {activeFile ? <span className="file-pill">Attached: {activeFile}</span> : null}
        <button type="button" className="secondary-btn" onClick={startNewChat}>New chat</button>
      </div>
      <div className="messages" aria-live="polite">
        {messages.map((msg, idx) => (
          <Message key={`${msg.role}-${idx}`} role={msg.role} text={msg.text} />
        ))}
        {loading && <Message role="assistant" text="Typing..." />}
        <div ref={bottomRef} />
      </div>

      <div className="composer-row">
        <label className="upload-btn">
          <input type="file" onChange={handleFileUpload} hidden />
          {uploading ? 'Uploading...' : 'Upload file'}
        </label>
        <form className="composer" onSubmit={handleSubmit}>
          <input
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder="Ask something like: get online data, summarize my files, or save chat history..."
          />
          <button type="submit" disabled={loading}>
            {loading ? 'Sending...' : 'Send'}
          </button>
        </form>
      </div>
    </div>
  )
}

export default ChatBox
