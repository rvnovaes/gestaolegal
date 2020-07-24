"""mudanca tbl assistido fisico

Revision ID: 08ab4edf9e63
Revises: 2ee9a443d882
Create Date: 2020-06-04 15:40:23.721016

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '08ab4edf9e63'
down_revision = '2ee9a443d882'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('assistidos_pessoa_fisica', 'gastos_medicacao',
               existing_type=mysql.VARCHAR(collation='latin1_general_ci', length=20),
               type_=sa.Integer(),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('assistidos_pessoa_fisica', 'gastos_medicacao',
               existing_type=sa.Integer(),
               type_=mysql.VARCHAR(collation='latin1_general_ci', length=20),
               existing_nullable=False)
    # ### end Alembic commands ###
