from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional, Dict, Any

VALID_PROJECT_STATUSES = {"active", "completed", "on_hold"}


@dataclass
class Project:
    """
    Класс, представляющий проект.
    """

    name: str
    description: str
    start_date: datetime
    end_date: datetime

    id: Optional[int] = field(default=None)
    status: str = field(default="active")

    def __post_init__(self) -> None:
        if self.status not in VALID_PROJECT_STATUSES:
            raise ValueError(f"invalid status: {self.status}")

        if not isinstance(self.start_date, datetime) or not isinstance(self.end_date, datetime):
            raise TypeError("start_date and end_date must be datetime instances")

        if self.end_date < self.start_date:
            raise ValueError("end_date must be greater than or equal to start_date")

    def update_status(self, new_status: str) -> None:
        """
        Обновляет статус проекта.
        """
        if new_status not in VALID_PROJECT_STATUSES:
            raise ValueError(f"invalid status: {new_status}")
        self.status = new_status

    def get_progress(self) -> float:
        """
        Примерная оценка прогресса проекта в процентах (0–100)
        по времени между start_date и end_date.

        Это не завязано на задачах, а только на датах.
        """
        now = datetime.now()

        if now <= self.start_date:
            return 0.0

        if now >= self.end_date:
            return 100.0

        total = (self.end_date - self.start_date).total_seconds()
        done = (now - self.start_date).total_seconds()

        if total <= 0:
            return 100.0

        return (done / total) * 100.0

    def to_dict(self) -> Dict[str, Any]:
        """
        Возвращает словарь с данными проекта.
        """
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "status": self.status,
        }
