"""create users

Revision ID: ac1f861d6578
Revises: eadd2785810e
Create Date: 2025-07-30 22:34:25.457399

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ac1f861d6578'
down_revision: Union[str, Sequence[str], None] = 'eadd2785810e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
