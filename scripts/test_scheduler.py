from app.scheduler.task_scheduler import TaskScheduler

scheduler = TaskScheduler()

scheduler.add_task("Retrieve Resume")
scheduler.add_task("Fetch Weather")
scheduler.add_task("Check Profile")

while scheduler.has_tasks():

    task = scheduler.get_next_task()

    print(task)