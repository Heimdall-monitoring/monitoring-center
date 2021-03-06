"""empty message

Revision ID: 558902804a6b
Revises: 
Create Date: 2020-09-21 18:08:08.277226

"""
import sqlalchemy as sa

from alembic import op


# revision identifiers, used by Alembic.
revision = '558902804a6b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Probes',
    sa.Column('uuid', sa.String(length=64), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=False),
    sa.Column('description', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('uuid')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Probes')
    # ### end Alembic commands ###
