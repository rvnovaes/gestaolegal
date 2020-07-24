"""Inclusao de Campos tb_Usuarios e alteracao de campos tb_Assistidos

Revision ID: 1af8ba45c38d
Revises: 1a9e33d26a93
Create Date: 2020-05-30 11:10:45.866376

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '1af8ba45c38d'
down_revision = '1a9e33d26a93'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('assistidos_pessoa_fisica', 'gastos_medicacao',
               existing_type=mysql.INTEGER(display_width=11),
               type_=sa.String(length=20, collation='latin1_general_ci'),
               existing_nullable=False)
    op.alter_column('assistidos_pessoa_juridica', 'faturamento_anual',
               existing_type=mysql.INTEGER(display_width=11),
               type_=sa.String(length=10, collation='latin1_general_ci'),
               existing_nullable=False)
    op.add_column('usuarios', sa.Column('cert_atuacao_DAJ', sa.String(length=3, collation='latin1_general_ci'), nullable=True))
    op.add_column('usuarios', sa.Column('ferias', sa.String(length=10, collation='latin1_general_ci'), nullable=True))
    op.add_column('usuarios', sa.Column('suplente', sa.String(length=30, collation='latin1_general_ci'), nullable=True))
    op.alter_column('usuarios', 'matricula',
               existing_type=mysql.VARCHAR(collation='latin1_general_ci', length=45),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('usuarios', 'matricula',
               existing_type=mysql.VARCHAR(collation='latin1_general_ci', length=45),
               nullable=False)
    op.drop_column('usuarios', 'suplente')
    op.drop_column('usuarios', 'ferias')
    op.drop_column('usuarios', 'cert_atuacao_DAJ')
    op.alter_column('assistidos_pessoa_juridica', 'faturamento_anual',
               existing_type=sa.String(length=10, collation='latin1_general_ci'),
               type_=mysql.INTEGER(display_width=11),
               existing_nullable=False)
    op.alter_column('assistidos_pessoa_fisica', 'gastos_medicacao',
               existing_type=sa.String(length=20, collation='latin1_general_ci'),
               type_=mysql.INTEGER(display_width=11),
               existing_nullable=False)
    # ### end Alembic commands ###
