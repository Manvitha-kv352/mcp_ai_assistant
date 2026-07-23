# 🤖 MCP Assistant

> An AI assistant that combines FastAPI, React, RAG, document understanding, and tool execution to build a practical conversational agent.

---

## Overview

MCP Assistant is a modular AI application that combines a React frontend with a FastAPI backend, document retrieval, and intelligent task planning.

It uses uploaded files and semantic search to provide context-aware responses, while an agent planner decides whether to answer directly, use retrieval, or execute a tool.

---

## Key Features

- Conversational AI with file upload support
- PDF document parsing and semantic search
- Retrieval-Augmented Generation (RAG)
- Session-based conversation memory
- FastAPI backend API
- React + Vite frontend
- ChromaDB local vector store
- Groq / Ollama LLM integration
- Docker-ready deployment
- Render deployment support

---

## Architecture

```text
User
 ├─ React frontend
 │    ├─ /chat
 │    └─ /upload
 └─ FastAPI backend
      ├─ session manager
      ├─ planner agent
      ├─ RAG agent
      ├─ MCP tools
      ├─ ChromaDB
      └─ LLM client (Groq / Ollama)
```

---

## Project Structure

```text
mcp_ai_assistant/
├── app/
│   ├── agents/
│   ├── api/
│   ├── llm/
│   ├── rag/
│   ├── session/
│   ├── services/
│   └── main.py
├── frontend/
├── chroma_db/
├── uploads/
├── Dockerfile
├── requirements.txt
├── render.yaml
└── README.md
```

---

## Quick Start

### 1. Create environment

```bash
python -m venv .venv
.venv\Scripts\activate    # Windows
# source .venv/bin/activate # Linux / macOS
```

### 2. Install backend dependencies

```bash
pip install -r requirements.txt
```

### 3. Install frontend dependencies

```bash
cd frontend
npm install
cd ..
```

### 4. Configure environment

Create a `.env` file in the repo root with:

```dotenv
supabase_url=https://your-supabase-url
supabase_key=your-supabase-key
groq_api_key=your-groq-api-key
# or use GROK_API_KEY in environment variables
```

### 5. Run backend

```bash
uvicorn app.main:app --reload --host 127.0.0.1 --port 8013
```

### 6. Run frontend

```bash
cd frontend
npm run dev
```

Open the app at `http://127.0.0.1:5174`.

---

## API Endpoints

- `GET /` — root welcome message
- `GET /health` — health check
- `POST /chat` — send a chat message
- `POST /upload` — upload a PDF file

---

## Deployment

### Render

This repository includes `render.yaml` for Render deployment.

- Backend: Docker web service using `Dockerfile`
- Frontend: Static site built from `frontend`

### Required Render environment variables

- `GROQ_API_KEY` or `GROK_API_KEY`
- `SUPABASE_URL`
- `SUPABASE_KEY`

### Docker

The backend Docker image is built from `Dockerfile`.

If you prefer to deploy on Render with Docker, use the `render.yaml` manifest.

---

## Notes

- The frontend expects `VITE_API_BASE_URL` only if you want to override the default API host.
- The backend defaults to `groq_api_key` and `grok_api_key`.
- Uploaded PDFs are indexed into ChromaDB for semantic retrieval.

---

## Troubleshooting

- If the backend cannot bind to `8013`, stop any existing Python/Uvicorn process using that port.
- If CORS fails in the browser, confirm the frontend and backend are running on the expected hosts and the backend is restarted.
- If the LLM returns fallback embeddings, ensure your Groq API key is configured and valid.

---

## Good to Know

This app is designed to let you:

- chat naturally
- upload documents for context
- build on top of a modular AI workflow

For best results, deploy the backend and frontend separately in Render, and use the `.env` / Render environment variables for keys.

```

Backend:

```
http://localhost:8013
```

## Run Frontend

```bash
cd frontend
npm install
npm run dev
```

Frontend:

```
http://localhost:5174
```

---

#  Docker

```bash
docker compose up --build
```

---

#  Demo

*(Add screenshots or a GIF here.)*

Recommended screenshots:

- Home Page
- Chat Interface
- Document Upload
- RAG Retrieval
- Generated Response

---

#  Example Use Cases

- Question answering over uploaded PDFs
- AI-powered research assistant
- Enterprise document search
- Internal knowledge base assistant
- Customer support knowledge retrieval
- Technical documentation assistant

---

#  Learning Outcomes

This project demonstrates practical experience with:

- Agentic AI systems
- Model Context Protocol (MCP)
- Retrieval-Augmented Generation (RAG)
- LangChain orchestration
- FastAPI backend development
- React frontend development
- ChromaDB vector search
- Local Large Language Models
- Docker containerization
- Modular AI architecture

---

#  Future Improvements

- User authentication
- Multi-user support
- Persistent chat history
- Supabase integration
- Streaming AI responses
- Voice interaction
- Image understanding
- Cloud deployment
- Multi-agent collaboration
- Workflow visualization dashboard

---

#  Author

**Manvitha KV**

B.E. Artificial Intelligence & Data Science

GitHub: https://github.com/Manvitha-kv352


---

## ⭐ If you found this project useful, consider giving it a star!
