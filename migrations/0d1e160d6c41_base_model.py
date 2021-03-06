"""base_model

Revision ID: 0d1e160d6c41
Revises: 79cefec5be09
Create Date: 2020-01-24 15:55:25.015508

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "0d1e160d6c41"
down_revision = "79cefec5be09"
branch_labels = ()
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "secapproval_requests",
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=True),
    )

    op.execute("UPDATE secapproval_requests SET updated_at = now()")
    op.alter_column("secapproval_requests", "updated_at", nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("secapproval_requests", "updated_at")
    # ### end Alembic commands ###
