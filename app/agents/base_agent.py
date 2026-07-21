from abc import ABC, abstractmethod


class BaseAgent(ABC):

    @abstractmethod
    async def execute(self, task, context):
        """
        Execute a task assigned to the agent.

        Args:
            task: Task object containing the agent name, input, metadata, etc.
            context: Shared workflow context (conversation history, config, memory, etc.)

        Returns:
            dict: Standardized agent response.
        """
        pass