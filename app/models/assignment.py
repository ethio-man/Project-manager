from sqlmodel import SQLModel,Field,Relationship
from typing import Optional,TYPE_CHECKING
from datetime import datetime

if TYPE_CHECKING:
    from app.models.employee import Employee
    from app.models.project import Project

class Assignment(SQLModel,table=True):
    id:Optional[int]=Field(default=None,primary_key=True)
    employee_id:int=Field(foreign_key='employee.id')
    project_id:int=Field(foreign_key='project.id')
    hours_allocated:int
    assigned_at:datetime=Field(default_factory=datetime.utcnow)

    employee:Optional['Employee']=Relationship(back_populates='assignments')
    project:Optional['Project']=Relationship()