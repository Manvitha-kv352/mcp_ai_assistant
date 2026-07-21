from app.process.task import Task
from app.process.process_manager import ProcessManager

manager = ProcessManager()

manager.add_task(
    Task(
        agent="RAG",
        action="retrieve_resume",
        data="Summarize my resume"
    )
)

results = manager.run()

for item in results:
    print(item["task"])
    print(item["result"])