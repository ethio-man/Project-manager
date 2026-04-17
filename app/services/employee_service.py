from sqlmodel import Session, select
from sqlalchemy import func

from app.models.employee import Employee
from app.models.assignment import Assignment
from app.models.project import Project
from app.utils.enum import ProjectStatus

#Redis will be implemented here later
def get_employee_workload(db: Session):
    statement = (
        select(
            Employee,
            func.count(Project.id).label("active_projects")
        )
        .select_from(Employee)
        .outerjoin(Assignment, Assignment.employee_id == Employee.id)
        .outerjoin(
            Project,
            (Project.id == Assignment.project_id)
            & (Project.status == ProjectStatus.ACTIVE),
        )
        .group_by(Employee.id)
    )

    results = db.exec(statement).all()

    return [
        {
            "id": emp.id,
            "name": emp.name,
            "email": emp.email,
            "role": emp.role,
            "active_projects": int(count),
        }
        for emp, count in results
    ]
