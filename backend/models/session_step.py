from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from core.database import Base


class SessionStep(Base):
    """SQLAlchemy model for session_steps table."""

    __tablename__ = "session_steps"

    id = Column(Integer, primary_key=True, index=True)
    step_id = Column(Integer, ForeignKey("steps.id"), nullable=False)
    prep_session_id = Column(Integer, ForeignKey("prep_sessions.id"), nullable=False)
    start_time = Column(DateTime(timezone=True), nullable=True)
    end_time = Column(DateTime(timezone=True), nullable=True)
    total_duration_seconds = Column(Integer, nullable=True)

    # Relationships
    step = relationship("Step", back_populates="session_steps")
    prep_session = relationship("PrepSession", back_populates="session_steps")
