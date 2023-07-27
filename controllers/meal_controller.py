from flask import Blueprint, request
from init import db
from models.meal import Meal, meals_schema, meal_schema

meals_bp = Blueprint('meals', __name__, url_prefix='/meals')

@meals_bp.route('/')
def get_all_meals():
    stmt = db.select(Meal).order_by(Meal.meal_name.desc())
    meals = db.session.scalars(stmt)
    return meals_schema.dump(meals)