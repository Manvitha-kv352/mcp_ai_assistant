# 🤖 MCP Assistant

An AI-powered **Model Context Protocol (MCP) Assistant** built with **FastAPI**, **React (Vite)**, and **Ollama**. The application enables intelligent conversations, document-based question answering using **Retrieval-Augmented Generation (RAG)**, and integration with external tools for file, API, and database operations.

---

## 🚀 Features

* 🤖 AI-powered conversational assistant using **Ollama**
* 🧠 Supports local LLMs such as **Llama 3** and **Mistral**
* 📄 Upload and analyze PDF documents
* 🔍 Retrieval-Augmented Generation (RAG) for document question answering
* 🛠️ Extensible Model Context Protocol (MCP) tool integration
* 💬 Session-based chat history
* 🆕 Start a new chat anytime
* ⚡ FastAPI backend with React + Vite frontend
* 🐳 Docker support for containerized deployment
* 📂 Local document indexing for contextual responses

---

# 🏗️ Project Architecture

```text
mcp_ai_assistant/
│
├── app/
│   ├── agents/              # AI agent logic
│   ├── planner/             # Task planning
│   ├── rag/                 # Retrieval-Augmented Generation
│   ├── sessions/            # Session management
│   ├── tools/               # MCP tool handlers
│   ├── models/
│   └── main.py              # FastAPI entry point
│
├── frontend/                # React + Vite frontend
│
├── uploads/                 # Uploaded documents
├── outputs/                 # Generated outputs
├── chroma_db/               # Chroma vector database
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .gitignore
└── README.md
```

---

# 🛠️ Tech Stack

### Backend

* Python
* FastAPI
* Uvicorn
* LangChain
* ChromaDB
* Ollama

### Frontend

* React
* Vite
* JavaScript
* CSS

### AI & RAG

* Ollama
* Llama 3 / Mistral (configurable)
* Retrieval-Augmented Generation (RAG)

### Deployment

* Docker
* Docker Compose

---

# 📋 Prerequisites

Before running the project, install:

* Python 3.10+
* Node.js & npm
* Git
* Ollama
* Docker Desktop (optional)

---

# ⚙️ Installation

## 1. Clone the repository

```bash
git clone https://github.com/Manvitha-kv352/mcp_ai_assistant.git

cd mcp_ai_assistant
```

---

## 2. Create a virtual environment

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

## 3. Install backend dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Install and configure Ollama

Download Ollama:

https://ollama.com

Pull a supported model:

```bash
ollama pull llama3
```

or

```bash
ollama pull mistral
```

Start the Ollama server:

```bash
ollama serve
```

---

## 5. Start the backend

```bash
.\.venv\Scripts\python.exe -m uvicorn app.main:app --host 127.0.0.1 --port 8013 --log-level warning
```

Backend:

```text
http://localhost:8013
```

---

## 6. Start the frontend

Open another terminal:

```bash
cd frontend

npm install

npm run dev
```

Frontend:

```text
http://localhost:5174
```

---

# 🐳 Docker

Build and run the application:

```bash
docker compose up --build
```

Then open:

```text
http://localhost:8013
```

---

# 📖 Usage

1. Launch the backend.
2. Start the frontend.
3. Open the application in your browser.
4. Upload a PDF document.
5. Ask questions related to the uploaded document.
6. Continue the conversation with maintained session history.
7. Click **New Chat** to begin a fresh conversation.

---

# 🧠 How It Works

1. The user uploads a document.
2. The document is processed and indexed into **ChromaDB**.
3. Relevant document chunks are retrieved using **RAG**.
4. The retrieved context is combined with the user's query.
5. **Ollama** generates a context-aware response.
6. If needed, the planner routes requests to MCP tools for additional actions.

---

# 📂 Project Components

| Component    | Description                                   |
| ------------ | --------------------------------------------- |
| FastAPI      | Backend API server                            |
| React + Vite | Frontend user interface                       |
| Ollama       | Local Large Language Model                    |
| ChromaDB     | Vector database for document retrieval        |
| LangChain    | RAG pipeline and orchestration                |
| MCP Tools    | External API, file, and database integrations |

---

# 🌟 Future Enhancements

* User authentication
* Persistent chat history
* Supabase integration
* Multi-user support
* Streaming AI responses
* Additional MCP tool integrations
* Cloud deployment
* Voice interaction
* Image understanding
* Advanced document search

---

# 🤝 Contributing

Contributions are welcome!

1. Fork the repository.
2. Create a new feature branch.

```bash
git checkout -b feature-name
```

3. Commit your changes.

```bash
git commit -m "Add new feature"
```

4. Push your branch.

```bash
git push origin feature-name
```

5. Open a Pull Request.

---

# 📄 License

This project is licensed under the **MIT License**.

---

# 👩‍💻 Author

**Manvitha K V**

**B.Tech – Artificial Intelligence & Data Science**

GitHub: **https://github.com/Manvitha-kv352**

---

⭐ If you found this project useful, consider giving it a **star** on GitHub!
