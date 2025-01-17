"""empty message

Revision ID: 3557c92ab790
Revises: e878ae66f154
Create Date: 2024-01-20 21:26:10.100033

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = "3557c92ab790"
down_revision = "e878ae66f154"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("users", sa.Column("username", sa.String(length=30), nullable=False))
    op.drop_column("users", "name")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("users", sa.Column("name", mysql.VARCHAR(length=30), nullable=False))
    op.drop_column("users", "username")
    # ### end Alembic commands ###
