from pydantic import BaseModel
from datetime import datetime

class AssignmentCreate(BaseModel):
    employee_id:int
    project_id:int
    hours_allocated:int

class AssignmentRead(BaseModel):
    id:int
    employee_id:int
    project_id:int
    hours_allocated:int
    assigned_at:datetime