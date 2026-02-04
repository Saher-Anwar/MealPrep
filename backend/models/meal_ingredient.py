from sqlalchemy import Column, Integer, String, Text, Boolean, Float, ForeignKey
from sqlalchemy.orm import relationship
from core.database import Base


class MealIngredient(Base):
    """SQLAlchemy model for meal_ingredients table."""

    __tablename__ = "meal_ingredients"

    id = Column(Integer, primary_key=True, index=True)
    meal_id = Column(Integer, ForeignKey("meals.id"), nullable=False)
    ingredient_id = Column(Integer, ForeignKey("ingredients.id"), nullable=False)
    quantity = Column(Float, nullable=False)
    is_optional = Column(Boolean, default=False, nullable=False)
    preparation_notes = Column(Text, nullable=True)
    measurement_unit = Column(String(50), nullable=True)  # e.g. "tsp", "tbsp"

    # Relationships
    meal = relationship("Meal", back_populates="meal_ingredients")
    ingredient = relationship("Ingredient", back_populates="meal_ingredients")
