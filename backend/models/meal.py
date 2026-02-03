from sqlalchemy import Column, Integer, String, Text, Boolean, Float, ForeignKey
from sqlalchemy.orm import relationship
from core.database import Base


class Meal(Base):
    """SQLAlchemy model for meals table."""

    __tablename__ = "meals"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, index=True)
    description = Column(Text, nullable=True)
    image = Column(String(500), nullable=True)
    category = Column(String(255), nullable=True)

    estimated_time = Column(Integer, nullable=True)  # minutes
    shelf_life_days = Column(Integer, nullable=True)

    # Creator
    creator_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    # Self-referencing parent meal
    parent_meal_id = Column(Integer, ForeignKey("meals.id"), nullable=True)

    # Cooking details
    cookware = Column(String(50), nullable=True)  # e.g. "oven", "microwave"
    is_public = Column(Boolean, default=False, nullable=False)
    is_custom = Column(Boolean, default=True, nullable=False)

    # Ratings & details
    servings = Column(Integer, nullable=True)
    difficulty_level = Column(Integer, nullable=True)  # 1-5
    specificity_rating = Column(Float, nullable=True)  # 0-5
    meal_rating = Column(Float, nullable=True)  # 0-5
    time_cooked = Column(Integer, nullable=True)  # minutes

    # Relationships
    creator = relationship("User", back_populates="custom_meals")
    parent_meal = relationship("Meal", remote_side=[id], backref="variations")
    steps = relationship("Step", back_populates="meal", order_by="Step.step_number")
    meal_ingredients = relationship("MealIngredient", back_populates="meal")
    ingredient_substitutions = relationship("IngredientSubstitution", back_populates="meal")
    prep_sessions = relationship("PrepSession", back_populates="meal")
