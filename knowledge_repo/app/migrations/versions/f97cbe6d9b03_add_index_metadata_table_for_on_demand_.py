"""Add index metadata table for on-demand reindexing.

Revision ID: f97cbe6d9b03
Revises: 36baffc5df12
Create Date: 2016-11-03 22:00:52.257484

"""

# revision identifiers, used by Alembic.
revision = 'f97cbe6d9b03'
down_revision = '36baffc5df12'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table('index_metadata',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type', sa.String(length=255), nullable=False),
    sa.Column('name', sa.String(length=512), nullable=False),
    sa.Column('value', sa.String(length=512), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('index_metadata')
