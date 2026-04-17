from typing import TYPE_CHECKING, Optional

from sqlmodel import Field, Relationship, SQLModel
from datetime import datetime

from app.models.base import IDMixin, TimestampMixin

if TYPE_CHECKING:
    from app.models.employee import Employee
    from app.models.project import Project

class Assignment(IDMixin, TimestampMixin, SQLModel, table=True):
    employee_id: int = Field(foreign_key='employee.id')
    project_id: int = Field(foreign_key='project.id')
    hours_allocated: int
    assigned_at: datetime = Field(default_factory=datetime.utcnow)

    employee: Optional['Employee'] = Relationship(back_populates='assignments')
    project: Optional['Project'] = Relationship(back_populates='assignments')