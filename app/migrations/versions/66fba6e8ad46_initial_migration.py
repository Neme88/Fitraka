"""initial migration

Revision ID: 66fba6e8ad46
Revises: 
Create Date: 2023-08-29 13:12:07.814884

"""
from alembic import op
import sqlalchemy as sa

# Import SQLAlchemy models
from app.models.models import User
from app.models.profile_model import profile 
from app.models.track_exercise_model import track_exercise

# revision identifiers, used by Alembic.
revision = '66fba6e8ad46'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # Create the User table
    op.create_table(
        'User',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('username', sa.String(length=80), nullable=False),
        sa.Column('email', sa.String(length=120), nullable=False),
        sa.Column('password_hash', sa.String(length=128), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('username'),
        sa.UniqueConstraint('email')
    )

    # Create the Profile table
    op.create_table(
        'profile',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('full_name', sa.String(length=100), nullable=True),
        sa.Column('date_of_birth', sa.Date(), nullable=True),
        sa.Column('gender', sa.String(length=10), nullable=True),
        sa.Column('bio', sa.String(length=255), nullable=True),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('profile_picture', sa.String(length=255), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('user_id'),
        sa.ForeignKeyConstraint(['user_id'], ['User.id'], ),
    )

    # Create the TrackExercise table
    op.create_table(
        'track_exercise',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('exercise_name', sa.String(length=100), nullable=False),
        sa.Column('duration_minutes', sa.Integer(), nullable=False),
        sa.Column('date_tracked', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
        sa.Column('calories_burned', sa.Float(), nullable=True),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.ForeignKeyConstraint(['user_id'], ['User.id'], ),
    )

    # Add foreign key constraints for the relationships
    op.create_foreign_key('fk_profile_user_id', 'profile', 'User', ['user_id'], ['id'])
    op.create_foreign_key('fk_track_exercise_user_id', 'track_exercise', 'User', ['user_id'], ['id'])


def downgrade():
    # Drop the foreign key constraints first
    op.drop_constraint('fk_track_exercise_user_id', 'track_exercise', type_='foreignkey')
    op.drop_constraint('fk_profile_user_id', 'profile', type_='foreignkey')

    # Then drop the tables in reverse order
    op.drop_table('track_exercise')
    op.drop_table('profile')
    op.drop_table('User')

