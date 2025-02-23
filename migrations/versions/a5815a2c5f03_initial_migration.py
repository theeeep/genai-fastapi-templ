"""initial_migration

Revision ID: a5815a2c5f03
Revises: 
Create Date: 2025-02-23 22:24:14.253261

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a5815a2c5f03'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_products_id', table_name='products')
    op.drop_table('products')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('products',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('title', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.Column('price', sa.NUMERIC(precision=10, scale=2), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='products_pkey')
    )
    op.create_index('ix_products_id', 'products', ['id'], unique=False)
    # ### end Alembic commands ###
