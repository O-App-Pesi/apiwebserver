from flask import Blueprint, request
from init import db
from models.diary_entry import DiaryEntry, diary_entry_schema, diary_entries_schema
from flask_jwt_extended import get_jwt_identity, jwt_required

diary_entry_bp = Blueprint('diary_entries', __name__, url_prefix='/diaryentry')

@diary_entry_bp.route('/')
def get_all_diary_entries():
    stmt = db.select(DiaryEntry)
    diary_entries = db.session.scalars(stmt)
    return diary_entries_schema.dump(diary_entries)

@diary_entry_bp.route('/<int:diaries_diary_id>/<int:meals_meal_id>/<int:health_analysis_ha_id>')
def get_one_diary_entry(diaries_diary_id, meals_meal_id, health_analysis_ha_id):
    filter_data = {'diaries_diary_id': diaries_diary_id, 'meals_meal_id': meals_meal_id, 'health_analysis_ha_id': health_analysis_ha_id}
    filter_data = {key: value for (key, value) in filter_data.items() if value}
    stmt = db.select(DiaryEntry).filter_by(**filter_data)

    diary_entry = db.session.scalar(stmt) #single scalar
    if diary_entry:
        return diary_entry_schema.dump(diary_entry)
    else:
        return {'error': 'An entry was not found with one or more specified ids'}, 404
    
@diary_entry_bp.route('/', methods=['POST'])
@jwt_required()
def create_diary_entry():
    body_data = request.get_json()
    diary_entry = DiaryEntry(
        diaries_diary_id=body_data.get('diaries_diary_id'),
        meals_meal_id=body_data.get('meals_meal_id'),
        health_analysis_ha_id=body_data.get('health_analysis_ha_id'),
        timestamp=body_data.get('timestamp')
    )
    db.session.add(diary_entry)
    db.session.commit()
    return diary_entry_schema.dump(diary_entry), 201

@diary_entry_bp.route('/<int:diaries_diary_id>/<int:meals_meal_id>/<int:health_analysis_ha_id>', methods=['DELETE'])
@jwt_required()
def delete_one_diary(diaries_diary_id, meals_meal_id, health_analysis_ha_id):
    filter_data = {'diaries_diary_id': diaries_diary_id, 'meals_meal_id': meals_meal_id, 'health_analysis_ha_id': health_analysis_ha_id}
    filter_data = {key: value for (key, value) in filter_data.items() if value}
    stmt = db.select(DiaryEntry).filter_by(**filter_data)
    diary_entry = db.session.scalar(stmt)
    if diary_entry:
        db.session.delete(diary_entry)
        db.session.commit()
        return {'message': f'Diary Entry with keys {diaries_diary_id}, {meals_meal_id}, {health_analysis_ha_id}, deleted'}
    else:
        return {'error': 'Diary not found with one or more specified IDs'}, 404
    
@diary_entry_bp.route('/<int:diaries_diary_id>/<int:meals_meal_id>/<int:health_analysis_ha_id>', methods=['PUT', 'PATCH'])
@jwt_required()
def update_one_diary(diaries_diary_id, meals_meal_id, health_analysis_ha_id):
    body_data = request.get_json()
    filter_data = {'diaries_diary_id': diaries_diary_id, 'meals_meal_id': meals_meal_id, 'health_analysis_ha_id': health_analysis_ha_id}
    filter_data = {key: value for (key, value) in filter_data.items() if value}
    stmt = db.select(DiaryEntry).filter_by(**filter_data)
    diary_entry = db.session.scalar(stmt)
    if diary_entry:
        diary_entry.timestamp = body_data.get('timestamp') or diary_entry.timestamp
        diary_entry.diaries_diary_id=body_data.get('diaries_diary_id') or diary_entry.diaries_diary_id
        diary_entry.meals_meal_id=body_data.get('meals_meal_id') or diary_entry.meals_meal_id
        diary_entry.health_analysis_ha_id=body_data.get('health_analysis_ha_id') or diary_entry.health_analysis_ha_id
        db.session.commit()
        return diary_entry_schema.dump(diary_entry)
    else:
        return {'error': f'Diary not found with one or more specified IDs'}, 404