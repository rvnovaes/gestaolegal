"""ajustes em relacao a nullable

Revision ID: 6bd5fa1902be
Revises: 1af8ba45c38d
Create Date: 2020-05-30 12:29:43.332127

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '6bd5fa1902be'
down_revision = '1af8ba45c38d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('usuarios', 'cert_atuacao_DAJ',
               existing_type=mysql.VARCHAR(collation='latin1_general_ci', length=3),
               nullable=False)
    op.alter_column('usuarios', 'modificado',
               existing_type=mysql.DATETIME(),
               nullable=True)
    op.alter_column('usuarios', 'modificadopor',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('usuarios', 'modificadopor',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=False)
    op.alter_column('usuarios', 'modificado',
               existing_type=mysql.DATETIME(),
               nullable=False)
    op.alter_column('usuarios', 'cert_atuacao_DAJ',
               existing_type=mysql.VARCHAR(collation='latin1_general_ci', length=3),
               nullable=True)
    # ### end Alembic commands ###