from app.agents.planner_agent import PlannerAgent
from app.executor.task_executor import TaskExecutor
from app.memory.shared_memory import SharedMemory


class Orchestrator:

    def __init__(self):
        self.planner = PlannerAgent()
        self.executor = TaskExecutor()
        self.memory = SharedMemory()

    def route(self, user_query: str):

        # Store user request
        self.memory.set("user_query", user_query)

        # Planner creates a plan
        plan = self.planner.plan(user_query)

        self.memory.set("plan", plan)

        # Execute the task
        result = self.executor.execute(user_query)

        self.memory.set("result", result)

        return {
            "plan": plan,
            "answer": result
        }