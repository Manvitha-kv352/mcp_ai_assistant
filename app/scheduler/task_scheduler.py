class TaskScheduler:

    def __init__(self):
        self.queue = []

    def add_task(self, task):

        self.queue.append(task)

    def get_next_task(self):

        if not self.queue:
            return None

        return self.queue.pop(0)

    def has_tasks(self):

        return len(self.queue) > 0