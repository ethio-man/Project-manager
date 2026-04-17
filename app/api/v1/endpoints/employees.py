from fastapi import APIRouter,Depends
from sqlmodel import Session
from typing import List
from app.schemas.employee import EmployeeRead
from app.core.database import get_session
from app.services.employee_service import get_employee_workload

router =APIRouter()
@router.get("/workload",response_model=List[EmployeeRead])
def workload(db: Session = Depends(get_session)):
    return get_employee_workload(db)