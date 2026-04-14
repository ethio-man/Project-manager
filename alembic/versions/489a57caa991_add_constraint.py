"""add constraint

Revision ID: 489a57caa991
Revises: 51729ec15902
Create Date: 2026-04-06 17:42:59.116679

"""
from typing import Sequence, Union

from alembic import op


# revision identifiers, used by Alembic.
revision: str = '489a57caa991'
down_revision: Union[str, Sequence[str], None] = '51729ec15902'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_check_constraint(
        'ck_assignment_hours_allocated_positive',
        'assignment',
        'hours_allocated > 0'
    )

    # Insert default employees only if they are missing.
    op.execute("""
        INSERT INTO employee (name, email, role)
        SELECT values_data.name, values_data.email, values_data.role
        FROM (
            VALUES
                ('Admin', 'admin@test.com', 'System Admin'),
                ('Dagmawi', 'dagmawi@gmail.com', 'Dev'),
                ('Antehun', 'antehun@gmail.com', 'Designer')
        ) AS values_data(name, email, role)
        WHERE NOT EXISTS (
            SELECT 1
            FROM employee e
            WHERE e.email = values_data.email
        )
    """)

def downgrade() -> None:
    """Downgrade schema."""
    op.execute("""
        DELETE FROM employee
        WHERE email IN ('admin@test.com', 'dagmawi@gmail.com', 'antehun@gmail.com')
    """)

    op.drop_constraint(
        'ck_assignment_hours_allocated_positive',
        'assignment',
        type_='check'
    )
