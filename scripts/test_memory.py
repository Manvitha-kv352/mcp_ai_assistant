from app.memory.shared_memory import SharedMemory

memory = SharedMemory()

memory.set("task", "Summarize my resume")
memory.set("chunks", ["Python", "FastAPI", "ChromaDB"])

print(memory.get("task"))
print(memory.get("chunks"))
print(memory.all())