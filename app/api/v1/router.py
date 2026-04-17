from fastapi import APIRouter
from app.api.v1.endpoints import projects,assignments,employees

router=APIRouter()
router.include_router(projects.router,prefix='/projects',tags=['Projects'])
router.include_router(assignments.router,prefix='/assignments',tags=['Assignments'])
#router.include_router(employees.router,prefix='/employees',tags=['Employees'])