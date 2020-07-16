"""修改user表主键

Revision ID: 854ab66292ce
Revises: 
Create Date: 2020-07-16 18:02:24.588786

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '854ab66292ce'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('slol_id', sa.String(length=50), nullable=True),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('level', sa.Integer(), nullable=True),
    sa.Column('ranking', sa.Integer(), nullable=True),
    sa.Column('league_points', sa.Integer(), nullable=True),
    sa.Column('rank', sa.Integer(), nullable=True),
    sa.Column('icon_id', sa.Integer(), nullable=True),
    sa.Column('tier', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###
