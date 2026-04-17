from enum import StrEnum


class ProjectStatus(StrEnum):
	ACTIVE = "Active"
	COMPLETED = "Completed"
	ARCHIVED = "Archived"


class EmployeeRole(StrEnum):
	DEV = "Dev"
	DESIGNER = "Designer"
	PM = "PM"
	SYSTEM_ADMIN = "System Admin"
