from typing import List

from domain.entities.task import Task
from ports.repositories.task_repository import TaskRepository


class InMemoryTaskRepository(TaskRepository):
    tasks: List[Task] = []

    def save(self, task: Task):
        self.tasks.append(task)
        return task
