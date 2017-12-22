"""empty message

Revision ID: 3eed60e800b9
Revises: 0aa90148fa76
Create Date: 2017-08-13 14:46:07.818049

"""

# revision identifiers, used by Alembic.
revision = '3eed60e800b9'
down_revision = '0aa90148fa76'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('word',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('word', sa.String(), nullable=True),
    sa.Column('embedding', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('word')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('word')
    ### end Alembic commands ###
