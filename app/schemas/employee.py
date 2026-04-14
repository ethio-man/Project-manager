from pydantic import BaseModel, computed_field

class EmployeeRead(BaseModel):
    id: int
    name: str
    email: str
    role: str
    active_projects: int = 0

    @computed_field
    @property
    def is_overloaded(self) -> bool:
        return self.active_projects >= 3