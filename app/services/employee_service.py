from sqlmodel import Session, select
from sqlalchemy import func

from app.models.employee import Employee
from app.models.assignment import Assignment
from app.models.project import Project

//Redis will be implemented here later
def get_employee_workload(db: Session):
    statement = (
        select(
            Employee,
            func.count(Project.id).label("active_projects")
        )
        .join(Assignment)
        .join(Project)
        .where(Project.status == "Active")
        .group_by(Employee.id)
    )

    results = db.exec(statement).all()

    return [
        {
            "employee": emp,
            "active_projects": count
        }
        for emp, count in results
    ]
