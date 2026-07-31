import { useState, useEffect, useRef } from 'react'
import Message from './Message'
import { sendMessage, uploadFile } from '../services/api'

const DEFAULT_GREETING = 'Hi! How can I help you today?'
const HISTORY_KEY = 'mcp-chat-history'
const SESSION_PREFIX = 'mcp-session-messages-'

const loadStoredMessages = (sessionId) => {
  if (!sessionId) return null

  try {
    const saved = localStorage.getItem(`${SESSION_PREFIX}${sessionId}`)
    return saved ? JSON.parse(saved) : null
  } catch {
    return null
  }
}

const buildSessionTitle = (sessionMessages) => {
  const firstUserMessage = sessionMessages?.find((message) => message.role === 'user')
  const text = firstUserMessage?.text?.trim()

  if (!text) return 'New conversation'
  return text.length > 42 ? `${text.slice(0, 39)}...` : text
}

const buildSessionPreview = (sessionMessages) => {
  const lastAssistantMessage = [...(sessionMessages || [])].reverse().find((message) => message.role === 'assistant')
  const lastUserMessage = [...(sessionMessages || [])].reverse().find((message) => message.role === 'user')
  const text = lastAssistantMessage?.text?.trim() || lastUserMessage?.text?.trim()

  if (!text) return 'Start a new conversation.'
  return text.length > 90 ? `${text.slice(0, 87)}...` : text
}

const loadHistory = () => {
  if (typeof window === 'undefined') return []

  try {
    const history = localStorage.getItem(HISTORY_KEY)
    return history ? JSON.parse(history) : []
  } catch {
    return []
  }
}

function ChatBox() {
  const [messages, setMessages] = useState(() => {
    const savedSessionId = localStorage.getItem('mcp-session-id') || ''
    const storedMessages = loadStoredMessages(savedSessionId)
    return storedMessages?.length ? storedMessages : [{ role: 'assistant', text: DEFAULT_GREETING }]
  })
  const [input, setInput] = useState('')
  const [loading, setLoading] = useState(false)
  const [sessionId, setSessionId] = useState(() => localStorage.getItem('mcp-session-id') || '')
  const [uploading, setUploading] = useState(false)
  const [activeFile, setActiveFile] = useState('')
  const [history, setHistory] = useState(() => loadHistory())
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

  useEffect(() => {
    if (!sessionId) return

    localStorage.setItem(`${SESSION_PREFIX}${sessionId}`, JSON.stringify(messages))

    const sessionSummary = {
      id: sessionId,
      title: buildSessionTitle(messages),
      preview: buildSessionPreview(messages),
      updatedAt: Date.now(),
    }

    const nextHistory = [sessionSummary, ...loadHistory().filter((entry) => entry.id !== sessionId)]
      .slice(0, 8)

    localStorage.setItem(HISTORY_KEY, JSON.stringify(nextHistory))
    setHistory(nextHistory)
  }, [messages, sessionId])

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
    } catch {
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
      const message = err?.message || 'Upload failed. Please try again.'
      setMessages((prev) => [...prev, { role: 'assistant', text: `Upload failed: ${message}` }])
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
    setMessages([{ role: 'assistant', text: DEFAULT_GREETING }])
    setInput('')
  }

  return (
    <div className="chat-layout">
      <aside className="history-sidebar">
        <div className="history-sidebar-header">
          <span>Recent chats</span>
          <button type="button" className="secondary-btn" onClick={startNewChat}>New chat</button>
        </div>

        <div className="history-list">
          {history.length === 0 ? (
            <p className="history-empty">Your recent chats will appear here.</p>
          ) : (
            history.map((entry) => (
              <div key={entry.id} className="history-item">
                <span className="history-title">{entry.title}</span>
                <span className="history-preview">{entry.preview}</span>
                <span className="history-time">{new Date(entry.updatedAt).toLocaleString()}</span>
              </div>
            ))
          )}
        </div>
      </aside>

      <div className="chat-card">
        <div className="chat-toolbar">
          {activeFile && <span className="file-pill">{activeFile}</span>}
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
    </div>
  )
}

export default ChatBox
