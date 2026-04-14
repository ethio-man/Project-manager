from fastapi import APIRouter,Depends
from sqlmodel import Session

from app.core.database import get_session
from app.schemas.project import ProjectCreate, ProjectRead,ProjectUpdate
from app.schemas.employee import EmployeeRead
from app.services.project_service import create_project,get_project_team,update_project

router =APIRouter()

@router.post('/',response_model=ProjectRead)
def create_project_route(project:ProjectCreate,db:Session=Depends(get_session)):
    return create_project(db,project)

@router.get("/{project_id}/team", response_model=list[EmployeeRead])
def get_team(project_id: int, db: Session = Depends(get_session)):
    return get_project_team(db, project_id)

@router.patch("/{project_id}", response_model=ProjectRead)
def update_project_route(
    project_id: int,
    data: ProjectUpdate,
    db: Session = Depends(get_session)
):
    return update_project(db, project_id, data)