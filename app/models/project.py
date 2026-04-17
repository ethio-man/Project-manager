from typing import TYPE_CHECKING, List

from sqlalchemy import Column, Enum as SAEnum
from sqlmodel import Field, Relationship, SQLModel

from app.models.base import IDMixin, TimestampMixin
from app.utils.enum import ProjectStatus

if TYPE_CHECKING:
    from app.models.assignment import Assignment
    
class Project(IDMixin, TimestampMixin, SQLModel, table=True):
    name: str
    description: str
    status: ProjectStatus = Field(
        default=ProjectStatus.ACTIVE,
        sa_column=Column(
            SAEnum(
                ProjectStatus,
                name="projectstatus",
                values_callable=lambda enum_cls: [item.value for item in enum_cls],
                native_enum=False,
            ),
            nullable=False,
        ),
    )

    assignments: List['Assignment'] = Relationship(back_populates='project')
