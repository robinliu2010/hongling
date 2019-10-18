"""add image_url in models.py

Revision ID: e714c236b9f7
Revises: da22d83e1dba
Create Date: 2019-10-18 19:32:58.399890

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e714c236b9f7'
down_revision = 'da22d83e1dba'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('course', sa.Column('image_url', sa.String(length=256), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('course', 'image_url')
    # ### end Alembic commands ###
