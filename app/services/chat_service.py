from app.session.session_manager import SessionManager
from app.database.supabase_chat import SupabaseChatDB
from app.orchestrator.workflow_manager import WorkflowManager
from app.planner.planner_agent import PlannerAgent


class ChatService:

    def __init__(self):

        self.session_manager = SessionManager()

        self.chat_db = SupabaseChatDB()

        self.workflow = WorkflowManager()

        self.planner = PlannerAgent()


    async def generate_response(
        self,
        message: str,
        session_id: str
    ):

        self.session_manager.create_session(session_id)

        # Save user message

        self.session_manager.add_message(
            session_id,
            "user",
            message
        )


        self.chat_db.save_message(
            session_id,
            "user",
            message
        )


        # PLAN TASK
        tasks = self.planner.plan(message)


        print("PLANNER OUTPUT:", tasks)


        # RUN WORKFLOW

        workflow_context = await self.workflow.run(tasks)


        # Get response dynamically

        response = None


        for agent in [
            "MCP",
            "RAG"
        ]:

            output = workflow_context.get_output(agent)

            if output:

                response = output

                break


        if response is None:

            response = "Sorry, I couldn't generate a response."


        # Save assistant response

        self.session_manager.add_message(
            session_id,
            "assistant",
            response
        )


        self.chat_db.save_message(
            session_id,
            "assistant",
            str(response)
        )


        return response