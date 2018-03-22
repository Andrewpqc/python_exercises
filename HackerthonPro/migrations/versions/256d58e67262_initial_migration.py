"""initial migration

Revision ID: 256d58e67262
Revises: 
Create Date: 2017-10-21 16:04:37.301814

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '256d58e67262'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('allcomment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content', sa.Text(), nullable=True),
    sa.Column('movieid', sa.BigInteger(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_charset='utf8'
    )
    op.create_table('comments_des',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content_split', sa.Text(), nullable=True),
    sa.Column('pos_count', sa.Integer(), nullable=True),
    sa.Column('nag_count', sa.Integer(), nullable=True),
    sa.Column('emotion', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_charset='utf8'
    )
    op.create_table('movie',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('movieid', sa.BigInteger(), nullable=True),
    sa.Column('bigComment', sa.Text(), nullable=True),
    sa.Column('rate1', sa.Float(), nullable=True),
    sa.Column('rate2', sa.Float(), nullable=True),
    sa.Column('rate3', sa.Float(), nullable=True),
    sa.Column('rate4', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_charset='utf8'
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('movie')
    op.drop_table('comments_des')
    op.drop_table('allcomment')
    # ### end Alembic commands ###