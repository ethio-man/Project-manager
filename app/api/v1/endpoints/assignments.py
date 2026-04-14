from fastapi import APIRouter,Depends
from sqlmodel import Session

from app.core.database import get_session
from app.core.redis_client import delete_key
from app.schemas.assignment import AssignmentCreate,AssignmentRead
from app.services.assignment_service import create_assignment

router = APIRouter()

@router.post('/',response_model=AssignmentRead)
def create_assignment_route(data: AssignmentCreate,db: Session = Depends(get_session)):
    assignment = create_assignment(db, data)
    delete_key(f"project:{assignment.project_id}:team")
    return assignment