from app.memory.shared_memory import SharedMemory


class AgentCommunicator:

    def __init__(self):
        self.memory = SharedMemory()

    def send(self, sender: str, receiver: str, message):

        key = f"{sender}_to_{receiver}"

        self.memory.set(key, message)

    def receive(self, sender: str, receiver: str):

        key = f"{sender}_to_{receiver}"

        return self.memory.get(key)