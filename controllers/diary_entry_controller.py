from flask import Blueprint, request
from init import db
from models.diary_entry import DiaryEntry, diary_entry_schema, diary_entries_schema

diary_entry_bp = Blueprint('diary_entries', __name__, url_prefix='/diaryentry')

@diary_entry_bp.route('/')
def get_all_diary_entries():
    stmt = db.select(DiaryEntry)
    diary_entry = db.session.scalars(stmt)
    return diary_entries_schema.dump(diary_entry)

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
    
# @diaries_bp.route('/', methods=['POST'])
# @jwt_required()
# def create_diary():
#     body_data = request.get_json()
#     diary = Diary(
#         users_user_id=get_jwt_identity(),
#         diary_title=body_data.get('diary_title')
#     )
#     db.session.add(diary)
#     db.session.commit()
#     return diary_schema.dump(diary), 201

# @diaries_bp.route('/<int:diary_id>', methods=['DELETE'])
# def delete_one_diary(diary_id):
#     stmt = db.select(Diary).filter_by(diary_id=diary_id)
#     diary = db.session.scalar(stmt)
#     if diary:
#         db.session.delete(diary)
#         db.session.commit()
#         return {'message': f'Diary {diary.diary_title} deleted successfully'}
#     else:
#         return {'error': f'Diary not found with id {diary_id}'}, 404
    
# @diaries_bp.route('/<int:diary_id>', methods=['PUT', 'PATCH'])
# @jwt_required()
# def update_one_card(diary_id):
#     body_data = request.get_json()
#     stmt = db.select(Diary).filter_by(diary_id=diary_id)
#     diary = db.session.scalar(stmt)
#     if diary:
#         diary.diary_title = body_data.get('diary_title') or diary.diary_title
#         return diary_schema.dump(diary)
#     else:
#         return {'error': f'Diary not found with id {diary_id}'}, 404