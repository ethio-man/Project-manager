from fastapi import APIRouter,Depends
from sqlmodel import Session
from fastapi.encoders import jsonable_encoder

from app.core.database import get_session
from app.core.redis_client import get_json, set_json
from app.schemas.project import ProjectCreate, ProjectRead,ProjectUpdate
from app.schemas.employee import EmployeeRead
from app.services.project_service import create_project,get_project_team,update_project

router =APIRouter()

@router.post('/',response_model=ProjectRead)
def create_project_route(project:ProjectCreate,db:Session=Depends(get_session)):
    return create_project(db,project)

@router.get("/{project_id}/team", response_model=list[EmployeeRead])
def get_team(project_id: int, db: Session = Depends(get_session)):
    cache_key = f"project:{project_id}:team"
    cached_team = get_json(cache_key)
    if cached_team is not None:
        return cached_team

    team = get_project_team(db, project_id)
    set_json(cache_key, jsonable_encoder(team), ttl_seconds=120)
    return team

@router.patch("/{project_id}", response_model=ProjectRead)
def update_project_route(
    project_id: int,
    data: ProjectUpdate,
    db: Session = Depends(get_session)
):
    return update_project(db, project_id, data)