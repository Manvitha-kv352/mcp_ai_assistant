import asyncio
from app.executor.task_executor import TaskExecutor
from app.process.task import Task

async def main():
    task = Task('MCP', {'tool': 'api', 'method': 'execute', 'data': {'query': 'hi', 'url': 'https://jsonplaceholder.typicode.com/posts/1'}})
    executor = TaskExecutor()
    try:
        result = await executor.execute(task)
        print(type(result).__name__)
        print(result)
    except Exception as exc:
        print(type(exc).__name__, exc)
        raise

asyncio.run(main())
