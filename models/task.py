from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional, Dict, Any

# допустимые статусы задачи
VALID_TASK_STATUSES = {"pending", "in_progress", "completed"}


@dataclass
class Task:
    """
    Класс, представляющий задачу в системе.
    """

    title: str
    description: str
    priority: int
    due_date: datetime
    project_id: int
    assignee_id: int

    # генерируются/заполняются позже
    id: Optional[int] = field(default=None)
    status: str = field(default="pending")

    def __post_init__(self) -> None:
        """
        Дополнительная валидация данных после инициализации dataclass.
        """
        if self.priority not in (1, 2, 3):
            raise ValueError("priority must be 1 (high), 2 (medium) or 3 (low)")

        if self.status not in VALID_TASK_STATUSES:
            raise ValueError(f"invalid status: {self.status}")

        if not isinstance(self.due_date, datetime):
            raise TypeError("due_date must be an instance of datetime")

    def update_status(self, new_status: str) -> None:
        """
        Обновляет статус задачи.
        """
        if new_status not in VALID_TASK_STATUSES:
            raise ValueError(f"invalid status: {new_status}")
        self.status = new_status

    def is_overdue(self) -> bool:
        """
        Возвращает True, если задача просрочена и ещё не завершена.
        """
        if self.status == "completed":
            return False
        return datetime.now() > self.due_date

    def to_dict(self) -> Dict[str, Any]:
        """
        Возвращает словарь с данными задачи.
        """
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "priority": self.priority,
            "status": self.status,
            "due_date": self.due_date,
            "project_id": self.project_id,
            "assignee_id": self.assignee_id,
        }

