# 🤖 MCP Assistant

> **An Agentic AI-powered Model Context Protocol (MCP) Assistant that combines Large Language Models, Retrieval-Augmented Generation (RAG), document understanding, and intelligent tool execution to automate complex user tasks through a modular AI workflow.**

---

##  Overview

MCP Assistant is an AI-powered assistant designed to extend the capabilities of Large Language Models by integrating document retrieval, external tools, and autonomous task planning into a single intelligent workflow.

Instead of relying solely on an LLM, the assistant retrieves relevant context from uploaded documents, orchestrates reasoning through modular AI components, and executes external tools when required. This architecture enables more accurate, context-aware, and actionable responses.

---

##  Key Features

-  AI-powered conversational assistant
-  Upload and analyze PDF documents
-  Retrieval-Augmented Generation (RAG)
-  Context-aware document question answering
-  Model Context Protocol (MCP) tool integration
-  Local document indexing using ChromaDB
-  Session-based conversation history
-  Start new conversations anytime
-  FastAPI REST API
-  React + Vite frontend
-  Docker support
-  Modular architecture for future AI agent expansion

---

##  System Architecture

```text
                     User
                       │
                       ▼
                 React Frontend
                       │
                       ▼
                 FastAPI Backend
                       │
        ┌──────────────┼──────────────┐
        ▼              ▼              ▼
  Session Manager   RAG Pipeline   Planner Agent
        │              │              │
        │              ▼              ▼
        │        ChromaDB        MCP Tools
        │              │              │
        └──────────────┼──────────────┘
                       ▼
                  Ollama LLM
              (Llama 3 / Mistral)
                       │
                       ▼
                 Final Response
```

---

#  Workflow

## Step 1 — User Interaction

The user uploads a PDF document or submits a natural language query through the React interface.

---

## Step 2 — Document Processing

Uploaded documents are parsed, chunked, embedded, and indexed into ChromaDB for semantic retrieval.

---

## Step 3 — Context Retrieval

Relevant document chunks are retrieved using similarity search to provide context for the user's query.

---

## Step 4 — AI Reasoning

The Planner Agent determines whether the request requires:

- Retrieval-Augmented Generation
- Direct LLM reasoning
- External MCP tool execution

---

## Step 5 — Response Generation

The retrieved context is combined with the user's prompt and passed to Ollama (Llama 3 or Mistral) to generate an accurate, context-aware response.

---

## Step 6 — Tool Execution

When necessary, MCP tools perform external operations such as file handling, API interactions, or database access before returning the final response.

---

#  Tech Stack

| Category | Technologies |
|-----------|-------------|
| **Backend** | Python, FastAPI, Uvicorn |
| **Frontend** | React, Vite, JavaScript |
| **AI Framework** | LangChain |
| **LLM** | Ollama, Llama 3, Mistral |
| **Vector Database** | ChromaDB |
| **Document Retrieval** | Retrieval-Augmented Generation (RAG) |
| **Protocol** | Model Context Protocol (MCP) |
| **Deployment** | Docker, Docker Compose |
| **Version Control** | Git, GitHub |

---

#  Project Structure

```text
mcp_ai_assistant/

├── app/
│   ├── agents/
│   ├── planner/
│   ├── rag/
│   ├── sessions/
│   ├── tools/
│   ├── models/
│   └── main.py
│
├── frontend/
├── uploads/
├── outputs/
├── chroma_db/
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

#  Why This Architecture?

Traditional chatbots rely entirely on an LLM, which limits their ability to access external knowledge and perform actions.

MCP Assistant extends the capabilities of LLMs through a modular architecture that combines:

- Retrieval-Augmented Generation for document understanding
- ChromaDB for semantic search
- Planner-based task routing
- External tool execution via Model Context Protocol
- Session management for conversational memory

This design makes the assistant scalable, maintainable, and capable of solving real-world tasks beyond simple text generation.

---

#  Installation

## Clone Repository

```bash
git clone https://github.com/Manvitha-kv352/mcp_ai_assistant.git
cd mcp_ai_assistant
```

## Create Virtual Environment

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Linux/macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## Install Backend Dependencies

```bash
pip install -r requirements.txt
```

## Install Ollama

Download:

https://ollama.com

Pull a model:

```bash
ollama pull llama3
```

or

```bash
ollama pull mistral
```

Start Ollama:

```bash
ollama serve
```

## Run Backend

```bash
uvicorn app.main:app --reload
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
