"""Initial Migration

Revision ID: ae454d2df8c4
Revises: c3ac55425150
Create Date: 2018-11-25 19:29:55.821497

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ae454d2df8c4'
down_revision = 'c3ac55425150'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Newblog',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('actual_blog', sa.String(length=255), nullable=True),
    sa.Column('vote_count', sa.String(), nullable=True),
    sa.Column('published_On', sa.Date(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('comments', sa.String(length=255), nullable=True),
    sa.Column('date_created', sa.Date(), nullable=True),
    sa.Column('Newblog_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['Newblog_id'], ['Newblog.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('comments')
    op.drop_table('Newblog')
    # ### end Alembic commands ###
