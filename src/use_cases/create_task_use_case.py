from domain.entities.task import Task
from ports.repositories.task_repository import TaskRepository


class CreateTaskUseCase:
    
    def __init__(self, task_repository: TaskRepository):
        self.task_repository = task_repository

    def create(self):
        pass
