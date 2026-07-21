from app.planner.planner_agent import PlannerAgent


planner = PlannerAgent()


query = "Get information from https://jsonplaceholder.typicode.com/posts/1"


result = planner.plan(query)


print(result)