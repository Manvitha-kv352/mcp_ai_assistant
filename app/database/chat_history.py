import sqlite3


class ChatHistoryDB:

    def __init__(self):

        self.conn = sqlite3.connect(
            "chat_history.db",
            check_same_thread=False
        )

        self.cursor = self.conn.cursor()

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS chat_history(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            session_id TEXT,

            role TEXT,

            message TEXT
        )
        """)

        self.conn.commit()


    def save_message(
        self,
        session_id,
        role,
        message
    ):

        self.cursor.execute(
            """
            INSERT INTO chat_history
            (session_id, role, message)
            VALUES (?, ?, ?)
            """,
            (session_id, role, message)
        )

        self.conn.commit()


    def get_history(self, session_id):

        self.cursor.execute(
            """
            SELECT role, message
            FROM chat_history
            WHERE session_id=?
            ORDER BY id
            """,
            (session_id,)
        )

        return self.cursor.fetchall()