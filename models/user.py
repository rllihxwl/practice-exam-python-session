from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional, Dict, Any

VALID_USER_ROLES = {"admin", "manager", "developer"}


@dataclass
class User:
    """
    Класс, представляющий пользователя системы.
    """

    username: str
    email: str
    role: str

    id: Optional[int] = field(default=None)
    registration_date: datetime = field(default_factory=datetime.now)

    def __post_init__(self) -> None:
        if self.role not in VALID_USER_ROLES:
            raise ValueError(f"invalid role: {self.role}")

        if not isinstance(self.registration_date, datetime):
            raise TypeError("registration_date must be a datetime instance")

    def update_info(
        self,
        username: Optional[str] = None,
        email: Optional[str] = None,
        role: Optional[str] = None,
    ) -> None:
        """
        Обновляет информацию о пользователе. Любой из параметров можно не передавать.
        """
        if username is not None:
            self.username = username

        if email is not None:
            self.email = email

        if role is not None:
            if role not in VALID_USER_ROLES:
                raise ValueError(f"invalid role: {role}")
            self.role = role

    def to_dict(self) -> Dict[str, Any]:
        """
        Возвращает словарь с данными пользователя.
        """
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "role": self.role,
            "registration_date": self.registration_date,
        }
