"""add timestamps to core tables

Revision ID: 7b9a2a10f4c1
Revises: 197472701658
Create Date: 2026-04-17 00:00:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "7b9a2a10f4c1"
down_revision: Union[str, Sequence[str], None] = "197472701658"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    tables = ["project", "employee", "assignment"]

    for table_name in tables:
        op.add_column(
            table_name,
            sa.Column(
                "created_at",
                sa.DateTime(timezone=True),
                nullable=False,
                server_default=sa.text("now()"),
            ),
        )
        op.add_column(
            table_name,
            sa.Column(
                "updated_at",
                sa.DateTime(timezone=True),
                nullable=False,
                server_default=sa.text("now()"),
            ),
        )


def downgrade() -> None:
    tables = ["assignment", "employee", "project"]

    for table_name in tables:
        op.drop_column(table_name, "updated_at")
        op.drop_column(table_name, "created_at")
