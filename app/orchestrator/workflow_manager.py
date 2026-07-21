from app.process.process_manager import ProcessManager
from app.memory.context import AgentContext


class WorkflowManager:

    def __init__(self):

        self.process_manager = ProcessManager()


    async def run(self, tasks):

        # Create fresh context for every workflow
        context = AgentContext()

        context.tasks = tasks


        # Add tasks to scheduler
        for task in tasks:

            self.process_manager.add_task(task)


        # Execute tasks
        results = await self.process_manager.run()


        # Store outputs
        for item in results:

            task = item["task"]

            result = item["result"]


            if isinstance(result, dict):

                context.add_output(
                    task.agent,
                    result.get(
                        "result",
                        result
                    )
                )

            else:

                context.add_output(
                    task.agent,
                    result
                )


        return context