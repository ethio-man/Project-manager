from sqlmodel import Session,select
from fastapi import HTTPException

from app.models.assignment import Assignment
from app.models.project import Project
from app.models.employee import Employee
from app.schemas.assignment import AssignmentCreate
from app.utils.enum import ProjectStatus

def create_assignment(db:Session,data:AssignmentCreate):
    employee = db.get(Employee, data.employee_id)
    if not employee:
        raise HTTPException(status_code=404,detail="Employee not found")
    
    project=db.get(Project,data.project_id)
    if not project:
        raise HTTPException(status_code=404,detail='Project not found')
    if project.status in [ProjectStatus.COMPLETED, ProjectStatus.ARCHIVED]:
        raise HTTPException(status_code=400,detail='Cannot assign to inactive project')
    
    statement=(
        select(Assignment)
        .join(Project)
        .where(
            Assignment.employee_id==data.employee_id,
            Project.status==ProjectStatus.ACTIVE,
        )
    )
    active_assignments=db.exec(statement).all()

    if len(active_assignments) >=3:
        raise HTTPException(status_code=400,detail='Employee at maximum capacity')
    
    assignment=Assignment(**data.model_dump())

    db.add(assignment)
    db.commit()
    db.refresh(assignment)

    return assignment