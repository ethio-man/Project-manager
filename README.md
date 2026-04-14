# Week 2 project - Employee and Task Assignment 

## Objective
Build a system to manage **Projects**, **Employees**, and **Task Assignments**. You must implement complex relationships, custom validation logic, and automated database auditing.

---

## 1. The Data Schema (Entity Relationships)
* **Employee (Model):** `id`, `name`, `email`, `role` (e.g., 'Dev', 'Designer', 'PM').
* **Project (Model):** `id`, `name`, `description`, `status` (e.g., 'Active', 'Completed', 'Archived').
* **Assignment (Association Model):** A many-to-many link between Employees and Projects. 
    * *Extra Fields:* `hours_allocated`, `assigned_at`.
    * *Constraint:* An employee cannot be assigned to more than 3 'Active' projects at once.

---

## 2. Advanced Technical Requirements

### A. SQLAlchemy & SQLModel Complexity
* **Many-to-Many:** Implement the relationship between `Employee` and `Project` using an association table/model.
* **Cascades:** If a `Project` is deleted, all its `Assignments` must be deleted, but the `Employees` must remain.
* **Base Mixins:** Create a `TimestampMixin` with `created_at` and `updated_at` (using `func.now()`) and inherit it in all models.

### B. Business Logic (The "Catch")
* **Assignment Logic:** In your `POST /assignments/` endpoint, you must query the database to count the employee's current active projects. If it’s $\geq 3$, return a `400 Bad Request` with the message: *"Employee at maximum capacity."*
* **Project Status Guard:** Prevent adding assignments to a project if its status is 'Archived' or 'Completed'.

### C. Alembic Migrations
* **Seed Data:** Create a separate Alembic revision script that populates the database with 3 default roles and 1 "System Admin" user.
* **Manual Edits:** You must manually edit one migration file to add a `CheckConstraint` on the `hours_allocated` field (must be $> 0$).

---

## 3. The API Specs
* `GET /projects/{id}/team`: Returns a list of all employees assigned to a specific project.
* `GET /employees/workload`: Returns a list of employees and a count of their currently assigned active projects.
* `POST /projects/`: Create a project.
* `POST /assignments/`: The "Heavy Lifter" endpoint that handles the logic mentioned in Section 2B.

---

## 4. Engineering Standards (The "Rubric")
1.  **Dependency Injection:** Use a `get_db` generator with a `try/finally` block to ensure sessions are closed.
2.  **Pydantic Computed Fields:** Use `@computed_field` in Pydantic v2 to return a `is_overloaded` boolean on the Employee schema if they have 3 active projects.
3.  **Typed Returns:** Every FastAPI path operation must have a `response_model` defined.
4.  **Selective Updates:** The `PATCH` endpoints must use `exclude_unset=True` in Pydantic to allow partial updates.

---

## 5. Submission Requirements
1.  **The Code:** Clean, PEP 8 compliant code.
2.  **The Migration Tree:** A clean `alembic history`.
