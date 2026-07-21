import uuid


class Task:

    def __init__(
        self,
        agent,
        input_data,
        task_type="default",
        dependencies=None,
        metadata=None,
        priority=1
    ):

        self.task_id = str(uuid.uuid4())[:8]

        self.agent = agent

        self.input = input_data

        self.task_type = task_type

        self.dependencies = dependencies or []

        self.metadata = metadata or {}

        self.priority = priority

        self.status = "pending"


    def __repr__(self):

        return (
            f"Task("
            f"id={self.task_id}, "
            f"agent={self.agent}, "
            f"status={self.status})"
        )