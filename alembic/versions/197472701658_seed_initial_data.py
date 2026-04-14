"""seed initial data

Revision ID: 197472701658
Revises: 489a57caa991
Create Date: 2026-04-06 17:47:19.417394

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '197472701658'
down_revision: Union[str, Sequence[str], None] = '489a57caa991'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
