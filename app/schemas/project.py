from pydantic import BaseModel

class ProjectCreate(BaseModel):
    name:str
    description:str
    status:str

class ProjectRead(BaseModel):
    id:int
    name:str
    description:str
    status:str

class ProjectUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    status: str | None = None