"""initial

Revision ID: 0001_initial
Revises: 
Create Date: 2025-10-09 00:00:00.000000

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '0001_initial'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        'admin_users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('username', sa.String(128), nullable=False, unique=True),
        sa.Column('password_hash', sa.String(256), nullable=False),
        sa.Column('role', sa.String(64), nullable=False),
        sa.Column('created_at', sa.DateTime, server_default=sa.func.now())
    )
    op.create_table(
        'transactions',
        sa.Column('transaction_id', sa.String(64), primary_key=True),
        sa.Column('amount', sa.Numeric(12,2), nullable=False),
        sa.Column('method', sa.String(32), nullable=False),
        sa.Column('token', sa.Text, nullable=True),
        sa.Column('status', sa.String(32), nullable=False),
        sa.Column('created_at', sa.DateTime, server_default=sa.func.now())
    )
    op.create_table(
        'payment_links',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('transaction_id', sa.String(64), sa.ForeignKey('transactions.transaction_id')),
        sa.Column('link', sa.String(512)),
        sa.Column('expires_at', sa.DateTime)
    )

def downgrade():
    op.drop_table('payment_links')
    op.drop_table('transactions')
    op.drop_table('admin_users')
