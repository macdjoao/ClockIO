"""Initial migration.

Revision ID: 85ccada1ab3a
Revises: 
Create Date: 2022-09-01 01:07:13.516105

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '85ccada1ab3a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('employees',
    sa.Column('employee_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('employee_cpf', sa.String(length=11), nullable=False),
    sa.Column('employee_email', sa.String(), nullable=False),
    sa.Column('employee_name', sa.String(length=200), nullable=False),
    sa.Column('employee_password_hash', sa.String(), nullable=False),
    sa.Column('employee_first_access', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('employee_id'),
    sa.UniqueConstraint('employee_cpf'),
    sa.UniqueConstraint('employee_email')
    )
    op.create_table('clocks',
    sa.Column('clock_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('clock_employee_id', sa.Integer(), nullable=True),
    sa.Column('clock_input', sa.DateTime(), nullable=False),
    sa.Column('clock_output', sa.DateTime(), nullable=False),
    sa.Column('clock_extra', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['clock_employee_id'], ['employees.employee_id'], ),
    sa.PrimaryKeyConstraint('clock_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('clocks')
    op.drop_table('employees')
    # ### end Alembic commands ###
