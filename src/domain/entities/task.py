from uuid import UUID, uuid4
from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Task:
    title: str
    description: str
    user_id: UUID
    deadline: datetime
    is_completed: bool
    id: UUID = field(default_factory=uuid4)
