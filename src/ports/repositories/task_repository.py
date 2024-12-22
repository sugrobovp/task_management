from abc import ABC, abstractmethod

from domain.entities.task import Task


class TaskRepository(ABC):

    @abstractmethod
    def save(self, task: Task):
        pass
