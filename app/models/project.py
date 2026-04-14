from sqlmodel import SQLModel,Field,Relationship
from typing import Optional,List,TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.assignment import Assignment

class Project(SQLModel,table=True):
    id:Optional[int] =Field(default=None,primary_key=True)
    name:str
    description:str
    status:str

    assignments:List['Assignment']=Relationship(back_populates='project')   