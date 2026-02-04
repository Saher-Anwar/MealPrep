from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from core.database import Base


class Ingredient(Base):
    """SQLAlchemy model for ingredients table."""

    __tablename__ = "ingredients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, index=True)
    category = Column(String(255), nullable=False)

    # Relationships
    pantry_items = relationship("PantryItem", back_populates="ingredient")
    meal_ingredients = relationship("MealIngredient", back_populates="ingredient")
