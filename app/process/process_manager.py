from app.scheduler.task_scheduler import TaskScheduler
from app.executor.task_executor import TaskExecutor


class ProcessManager:

    def __init__(self):
        self.scheduler = TaskScheduler()
        self.executor = TaskExecutor()

    def add_task(self, task):
        self.scheduler.add_task(task)

    async def run(self):

        results = []

        while self.scheduler.has_tasks():

            task = self.scheduler.get_next_task()

            task.status = "running"

            result = await self.executor.execute(task)

            task.status = "completed"

            results.append({
                "task": task,
                "result": result
            })

        return results