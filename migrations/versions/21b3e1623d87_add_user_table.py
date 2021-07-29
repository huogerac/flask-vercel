"""add user table

Revision ID: 21b3e1623d87
Revises: 
Create Date: 2021-07-29 17:16:39.849429

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "21b3e1623d87"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("name", sa.String(length=128), nullable=False),
        sa.Column("email", sa.String(length=255), nullable=True),
        sa.Column("password", sa.String(length=128), nullable=True),
        sa.Column("avatar", sa.UnicodeText(), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
    )


def downgrade():
    op.drop_table("users")
