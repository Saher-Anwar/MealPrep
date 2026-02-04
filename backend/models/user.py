from sqlalchemy import Column, Integer, String, Boolean, JSON
from sqlalchemy.orm import relationship
from core.database import Base


class User(Base):
    """SQLAlchemy model for users table."""

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False, index=True)
    inventory_update_mode = Column(Boolean, default=False, nullable=False)
    enable_pantry_tracking = Column(Boolean, default=False, nullable=False)
    notification_preferences = Column(JSON, nullable=True)
    unit_system = Column(String(50), default="metric", nullable=False)

    # Relationships
    pantry_items = relationship("PantryItem", back_populates="user")
    custom_meals = relationship("Meal", back_populates="creator")
    prep_sessions = relationship("PrepSession", back_populates="user")
