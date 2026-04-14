from fastapi import APIRouter
from app.api.v1.endpoints import projects,assignments,employees

api_router=APIRouter()
api_router.include_router(projects.router,prefix='/projects',tags=['Projects'])
api_router.include_router(assignments.router,prefix='/assignments',tags=['Assignments'])
#api_router.include_router(employees.router,prefix='/employees',tags=['Employees'])