from app.session.session_manager import SessionManager


manager = SessionManager()


session_id = manager.create_session()


print("Session ID:")
print(session_id)


manager.add_document(
    session_id,
    "resume.pdf"
)


manager.add_message(
    session_id,
    "user",
    "Summarize my resume"
)


manager.add_message(
    session_id,
    "assistant",
    "You have Python and FastAPI skills"
)


print(
    manager.get_session(session_id)
)