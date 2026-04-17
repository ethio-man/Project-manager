from pydantic import BaseModel

from app.utils.enum import ProjectStatus

class ProjectCreate(BaseModel):
    name:str
    description:str
    status: ProjectStatus

class ProjectRead(BaseModel):
    id:int
    name:str
    description:str
    status: ProjectStatus

class ProjectUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    status: ProjectStatus | None = None