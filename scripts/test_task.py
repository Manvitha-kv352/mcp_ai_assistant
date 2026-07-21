from app.process.task import Task

task = Task(
    agent="RAG",
    action="retrieve_resume",
    data="Summarize my resume"
)

print(task)