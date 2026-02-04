from sqlalchemy import Column, Integer, String, Text, Float, ForeignKey
from sqlalchemy.orm import relationship
from core.database import Base


class IngredientSubstitution(Base):
    """SQLAlchemy model for ingredient_substitutions table."""

    __tablename__ = "ingredient_substitutions"

    id = Column(Integer, primary_key=True, index=True)
    meal_id = Column(Integer, ForeignKey("meals.id"), nullable=False)
    original_ingredient_id = Column(Integer, ForeignKey("ingredients.id"), nullable=False)
    substitute_ingredient_id = Column(Integer, ForeignKey("ingredients.id"), nullable=False)
    conversion_ratio = Column(Float, nullable=True)
    notes = Column(Text, nullable=True)
    created_by_user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    # Relationships
    meal = relationship("Meal", back_populates="ingredient_substitutions")
    original_ingredient = relationship("Ingredient", foreign_keys=[original_ingredient_id])
    substitute_ingredient = relationship("Ingredient", foreign_keys=[substitute_ingredient_id])
    created_by = relationship("User")
