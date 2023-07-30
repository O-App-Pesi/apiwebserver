from flask import Blueprint, request
from init import db
from models.meal import Meal, meals_schema, meal_schema
from flask_jwt_extended import get_jwt_identity, jwt_required

meals_bp = Blueprint('meals', __name__, url_prefix='/meals')

#GET query, retrieves all entities from the meals table
@meals_bp.route('/')
def get_all_meals():
    stmt = db.select(Meal).order_by(Meal.meal_name.desc())
    meals = db.session.scalars(stmt)
    return meals_schema.dump(meals)

#GET query, retrieves one entity from the meals table based on the meal_id
@meals_bp.route('/<int:meal_id>')
def get_one_meal(meal_id):
    stmt = db.select(Meal).filter_by(meal_id=meal_id)
    meal = db.session.scalar(stmt) #single scalar
    if meal:
        return meal_schema.dump(meal)
    else:
        return {'error': f'Meal not found with id {meal_id}'}, 404
    
#POST query, adds a new entity to the meal table
#User must be logged in, action authenticated by jwt_required    
@meals_bp.route('/', methods=['POST'])
@jwt_required()
def create_meal():
    body_data = request.get_json()
    meal = Meal(
        users_user_id=get_jwt_identity(),
        meal_name=body_data.get('meal_name'),
        is_takeaway=body_data.get('is_takeaway'),
        kilojoules=body_data.get('kilojoules'),
        notes=body_data.get('notes')
    )
    db.session.add(meal)
    db.session.commit()
    return meal_schema.dump(meal), 201

#DELETE query, deletes an entity from the meals table based on the meal_id
#User must be logged in, action authenticated by jwt_required    
@meals_bp.route('/<int:meal_id>', methods=['DELETE'])
@jwt_required()
def delete_one_meal(meal_id):
    stmt = db.select(Meal).filter_by(meal_id=meal_id)
    meal = db.session.scalar(stmt)
    if meal:
        db.session.delete(meal)
        db.session.commit()
        return {'message': f'Meal: {meal.meal_name} deleted successfully'}
    else:
        return {'error': f'Meal not found with id {meal_id}'}, 404
    
#PUT/PATCH query, updates an entity in the meals table based on the meal_id
#User must be logged in, action authenticated by jwt_required    
@meals_bp.route('/<int:meal_id>', methods=['PUT', 'PATCH'])
@jwt_required()
def update_one_card(meal_id):
    body_data = request.get_json()
    stmt = db.select(Meal).filter_by(meal_id=meal_id)
    meal = db.session.scalar(stmt)
    if meal:
        meal.meal_name = body_data.get('meal_name') or meal.meal_title
        meal.is_takeaway = body_data.get('is_takeaway') or meal.is_takeaway
        meal.kilojoules = body_data.get('kilojoules') or meal.kilojoules
        meal.notes = body_data.get('notes') or meal.notes
        db.session.commit()
        return meal_schema.dump(meal)
    else:
        return {'error': f'Meal not found with id {meal_id}'}, 404
