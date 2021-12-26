"""empty message

Revision ID: 4981a5429021
Revises: 
Create Date: 2021-12-25 20:32:32.429907

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4981a5429021'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'telefones',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('telefone', sa.String(50), nullable=False),
    )
    pass


def downgrade():
    op.drop_table('telefones')
    pass
