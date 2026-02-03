from sqlalchemy import Column, Integer, String, Text, Float, ForeignKey
from sqlalchemy.orm import relationship
from core.database import Base


class Step(Base):
    """SQLAlchemy model for steps table."""

    __tablename__ = "steps"

    id = Column(Integer, primary_key=True, index=True)
    meal_id = Column(Integer, ForeignKey("meals.id"), nullable=False)
    step_number = Column(Integer, nullable=False)
    instruction = Column(Text, nullable=False)
    estimated_duration = Column(Integer, nullable=True)  # minutes
    heat_level = Column(String(50), nullable=True)
    oven_temp = Column(Float, nullable=True)

    # Relationships
    meal = relationship("Meal", back_populates="steps")
    session_steps = relationship("SessionStep", back_populates="step")
