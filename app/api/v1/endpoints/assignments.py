from fastapi import APIRouter,Depends
from sqlmodel import Session

from app.core.database import get_session
from app.schemas.assignment import AssignmentCreate,AssignmentRead
from app.services.assignment_service import create_assignment

router = APIRouter()

@router.post('/',response_model=AssignmentRead)
def create_assignment_route(data: AssignmentCreate,db: Session = Depends(get_session)):
    return create_assignment(db, data)