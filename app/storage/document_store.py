class DocumentStore:

    def __init__(self):

        self.documents = {}


    def add_document(
        self,
        session_id,
        filename
    ):

        if session_id not in self.documents:
            self.documents[session_id] = []

        self.documents[session_id].append(
            filename
        )


    def get_documents(
        self,
        session_id
    ):

        return self.documents.get(
            session_id,
            []
        )