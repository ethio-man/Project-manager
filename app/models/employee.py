from sqlmodel import SQLModel,Field,Relationship
from typing import Optional,List,TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.assignment import Assignment

class Employee(SQLModel,table=True):
    id:Optional[int]=Field(default=None,primary_key=True)
    name:str
    email:str
    role:str

    assignments:List['Assignment']=Relationship(back_populates='employee')