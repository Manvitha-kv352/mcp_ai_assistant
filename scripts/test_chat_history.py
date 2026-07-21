from app.database.chat_history import ChatHistoryDB


db = ChatHistoryDB()


session = "session1"


db.save_message(
    session,
    "user",
    "Summarize my resume"
)

db.save_message(
    session,
    "assistant",
    "You have Python, FastAPI and AI skills."
)


history = db.get_history(session)

for role, message in history:
    print(role, ":", message)