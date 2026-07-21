from app.executor.task_executor import TaskExecutor

executor = TaskExecutor()

question = input("Ask something: ")

result = executor.execute(question)

print("\nAnswer:\n")
print(result)