"""Renaming students to scholars

Revision ID: 29ed11af5427
Revises: 791279dd0760
Create Date: 2023-12-18 11:32:23.858833

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '29ed11af5427'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
