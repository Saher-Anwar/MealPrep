from sqlalchemy import Column, Integer, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from core.database import Base


class PrepSession(Base):
    """SQLAlchemy model for prep_sessions table."""

    __tablename__ = "prep_sessions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    meal_id = Column(Integer, ForeignKey("meals.id"), nullable=False)
    servings = Column(Integer, nullable=True)
    scheduled_at = Column(DateTime(timezone=True), nullable=True)
    started_at = Column(DateTime(timezone=True), nullable=True)
    completed_at = Column(DateTime(timezone=True), nullable=True)
    is_active = Column(Boolean, default=False, nullable=False)
    is_complete = Column(Boolean, default=False, nullable=False)
    total_duration_seconds = Column(Integer, nullable=True)

    # Relationships
    user = relationship("User", back_populates="prep_sessions")
    meal = relationship("Meal", back_populates="prep_sessions")
    session_steps = relationship("SessionStep", back_populates="prep_session")
