from fastapi import APIRouter,Depends
from sqlmodel import Session

from app.core.database import get_session
from app.services.employee_service import get_employee_workload

router =APIRouter()
@router.get("/workload")
def workload(db: Session = Depends(get_session)):
    return get_employee_workload(db)