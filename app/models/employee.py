from typing import TYPE_CHECKING, List

from sqlalchemy import Column, Enum as SAEnum
from sqlmodel import Field, Relationship, SQLModel

from app.models.base import IDMixin, TimestampMixin
from app.utils.enum import EmployeeRole

if TYPE_CHECKING:
    from app.models.assignment import Assignment

class Employee(IDMixin, TimestampMixin, SQLModel, table=True):
    name: str
    email: str
    role: EmployeeRole = Field(
        default=EmployeeRole.DEV,
        sa_column=Column(
            SAEnum(
                EmployeeRole,
                name="employeerole",
                values_callable=lambda enum_cls: [item.value for item in enum_cls],
                native_enum=False,
            ),
            nullable=False,
        ),
    )

    assignments: List['Assignment'] = Relationship(back_populates='employee')