from app.communication.agent_communicator import AgentCommunicator

comm = AgentCommunicator()

comm.send(
    "Planner",
    "RAG",
    "Retrieve the user's resume."
)

message = comm.receive(
    "Planner",
    "RAG"
)

print(message)