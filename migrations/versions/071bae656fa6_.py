"""empty message

Revision ID: 071bae656fa6
Revises: d5a2f39afc12
Create Date: 2020-02-26 17:25:06.347904

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '071bae656fa6'
down_revision = 'd5a2f39afc12'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('voters_table',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('poll_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['poll_id'], ['polls.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('polls', sa.Column('creator_user_id', sa.Integer(), nullable=True))
    op.add_column('polls', sa.Column('info_link', sa.String(length=200), nullable=True))
    op.add_column('polls', sa.Column('option1', sa.String(length=150), nullable=True))
    op.add_column('polls', sa.Column('option2', sa.String(length=150), nullable=True))
    op.add_column('polls', sa.Column('option3', sa.String(length=150), nullable=True))
    op.add_column('polls', sa.Column('option4', sa.String(length=150), nullable=True))
    op.add_column('polls', sa.Column('poll_description', sa.String(length=1000), nullable=True))
    op.add_column('polls', sa.Column('poll_question', sa.String(length=100), nullable=True))
    op.drop_constraint('polls_ibfk_1', 'polls', type_='foreignkey')
    op.create_foreign_key(None, 'polls', 'users', ['creator_user_id'], ['id'])
    op.drop_column('polls', 'poll_name')
    op.drop_column('polls', 'user_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('polls', sa.Column('user_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.add_column('polls', sa.Column('poll_name', mysql.VARCHAR(length=40), nullable=True))
    op.drop_constraint(None, 'polls', type_='foreignkey')
    op.create_foreign_key('polls_ibfk_1', 'polls', 'users', ['user_id'], ['id'])
    op.drop_column('polls', 'poll_question')
    op.drop_column('polls', 'poll_description')
    op.drop_column('polls', 'option4')
    op.drop_column('polls', 'option3')
    op.drop_column('polls', 'option2')
    op.drop_column('polls', 'option1')
    op.drop_column('polls', 'info_link')
    op.drop_column('polls', 'creator_user_id')
    op.drop_table('voters_table')
    # ### end Alembic commands ###