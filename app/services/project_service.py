from sqlmodel import Session,select
from fastapi import HTTPException

from app.models.project import Project
from app.models.assignment import Assignment
from app.models.employee import Employee
from app.schemas.project import ProjectCreate,ProjectUpdate

def create_project(db:Session,project_data:ProjectCreate):
    project=Project(**project_data.model_dump())
    db.add(project)
    db.commit()
    db.refresh(project)
    return project

def get_project_team(db: Session, project_id: int):
    project = db.get(Project, project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    statement = (
        select(Employee)
        .join(Assignment)
        .where(Assignment.project_id == project_id)
    )

    employees = db.exec(statement).all()
    return employees

def update_project(db: Session, project_id: int, data: ProjectUpdate):
    project = db.get(Project, project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    update_data = data.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(project, key, value)

    db.add(project)
    db.commit()
    db.refresh(project)

    return project