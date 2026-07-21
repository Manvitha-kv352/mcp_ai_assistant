import ChatBox from './components/ChatBox'

function App() {
  return (
    <div className="app-shell">
      <header className="app-header">
        <div>
          <p className="eyebrow">AI assistant</p>
          <h1>MCP Assistant</h1>
        </div>
      </header>
      <ChatBox />
    </div>
  )
}

export default App
