import pytest

from adapters.repositories.task_repository.in_memory_repository import InMemoryTaskRepository


def test_try():
    assert True


@pytest.fixture
def task_repository():
    return InMemoryTaskRepository()