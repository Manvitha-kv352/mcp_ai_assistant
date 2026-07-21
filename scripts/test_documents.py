from app.storage.document_store import DocumentStore


store = DocumentStore()


store.add_document(
    "session1",
    "resume.pdf"
)


store.add_document(
    "session1",
    "project.pdf"
)


print(
    store.get_documents(
        "session1"
    )
)