class AgentContext:

    def __init__(self):

        self.session_id = None
        self.user_query = None

        self.tasks = []

        # Store all agent outputs
        self.outputs = {}

        self.final_response = None

    def add_output(self, agent, output):

        self.outputs[agent] = output

    def get_output(self, agent):

        return self.outputs.get(agent)