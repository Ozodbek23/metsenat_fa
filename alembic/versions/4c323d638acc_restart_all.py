"""restart all

Revision ID: 4c323d638acc
Revises: 
Create Date: 2023-10-03 15:32:49.280253

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4c323d638acc'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('institute',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=125), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_institute_id'), 'institute', ['id'], unique=False)
    op.create_table('sponsors',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('full_name', sa.String(length=125), nullable=True),
    sa.Column('phone_number', sa.String(length=13), nullable=True),
    sa.Column('payment_amount', sa.BigInteger(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_sponsors_full_name'), 'sponsors', ['full_name'], unique=False)
    op.create_index(op.f('ix_sponsors_id'), 'sponsors', ['id'], unique=False)
    op.create_table('student',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('full_name', sa.String(length=125), nullable=True),
    sa.Column('phone_number', sa.String(length=13), nullable=True),
    sa.Column('type', sa.Enum('bachelor', 'master', name='studenteducationtype'), nullable=True),
    sa.Column('institute', sa.Integer(), nullable=True),
    sa.Column('contract_amount', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['institute'], ['institute.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_student_id'), 'student', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_student_id'), table_name='student')
    op.drop_table('student')
    op.drop_index(op.f('ix_sponsors_id'), table_name='sponsors')
    op.drop_index(op.f('ix_sponsors_full_name'), table_name='sponsors')
    op.drop_table('sponsors')
    op.drop_index(op.f('ix_institute_id'), table_name='institute')
    op.drop_table('institute')
    # ### end Alembic commands ###