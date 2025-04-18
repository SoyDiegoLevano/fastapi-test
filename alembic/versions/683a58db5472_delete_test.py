"""delete test

Revision ID: 683a58db5472
Revises: f0d6266ac8f5
Create Date: 2025-03-28 09:30:00.876551

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '683a58db5472'
down_revision: Union[str, None] = 'f0d6266ac8f5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('products', 'test')
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('products', sa.Column('test', sa.VARCHAR(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
