from app.core.container import create_registry
from app.context.context_manager import ContextManager


class TaskExecutor:

    def __init__(self):

        self.registry = create_registry()
        self.context = ContextManager()

        print(
            "REGISTERED AGENTS:",
            self.registry.agents.keys()
        )


    async def execute(self, task):

        requested_agent = str(
            getattr(task, "agent", "") or ""
        ).strip()

        print(
            "REQUESTED AGENT:",
            requested_agent
        )

        agent_name = requested_agent.upper()
        task.agent = agent_name

        agent = self.registry.get(agent_name)

        if agent is None:
            for registered_name, registered_agent in self.registry.agents.items():
                if registered_name.upper() == agent_name:
                    agent = registered_agent
                    break

        if agent is None:
            raise ValueError(
                f"Unknown agent: {requested_agent}"
            )

        result = await agent.execute(
            task,
            self.context
        )

        return result