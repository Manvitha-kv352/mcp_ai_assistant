# MCP Assistant

MCP Assistant is a FastAPI + React/Vite chat application that can:
- answer general questions,
- route to MCP tools for API/database/file tasks,
- upload and index PDF-like documents for follow-up questions,
- keep chat history in a session and support a new-chat workflow.

## Project structure

- app/ — FastAPI backend, agents, planner, RAG logic, session handling
- frontend/ — Vite React frontend
- docker-compose.yml — Docker compose entrypoint
- Dockerfile — container build definition

## Prerequisites

- Python 3.10+
- Node.js and npm
- Optional: Docker Desktop if you want to use the container flow

## Run locally

### 1) Backend

From the project root:

```powershell
.\.venv\Scripts\python.exe -m uvicorn app.main:app --host 127.0.0.1 --port 8013 --log-level warning
```

### 2) Frontend

In a second terminal:

```powershell
cd frontend
npm install
npm run dev
```

Open:

- http://localhost:5174

## Docker option

If Docker Desktop is installed and running:

```powershell
docker compose up --build
```

Then open:

- http://localhost:8013

## Usage

1. Open the chat UI in the browser.
2. Upload a file using the Upload file button.
3. Ask a question about the uploaded file in the same chat session.
4. Use New chat to start a fresh thread.

## Notes

- The app uses local session storage in the browser for the active chat thread id.
- The backend uses the local upload folder and the in-memory session manager for the current run.
- If you want persistent storage across restarts, connect the Supabase-backed database modules later.
