import uuid


class SessionManager:

    def __init__(self):

        self.sessions = {}


    def create_session(self, session_id=None):

        if session_id is None:
            session_id = str(uuid.uuid4())

        if session_id not in self.sessions:
            self.sessions[session_id] = {
                "documents": [],
                "chat_history": [],
                "memory": {}
            }

        return session_id


    def get_session(self, session_id):

        if session_id is None:
            return None

        if session_id not in self.sessions:
            self.create_session(session_id)

        return self.sessions.get(session_id)


    def add_document(
        self,
        session_id,
        filename
    ):

        session = self.get_session(session_id)

        if session:

            session["documents"].append(filename)


    def add_message(
        self,
        session_id,
        role,
        content
    ):

        session = self.get_session(session_id)

        if session:

            session["chat_history"].append(
                {
                    "role": role,
                    "content": content
                }
            )