from flask import Blueprint, request
from init import db
from models.diary import Diary, diaries_schema, diary_schema
from flask_jwt_extended import get_jwt_identity, jwt_required

diaries_bp = Blueprint('diaries', __name__, url_prefix='/diary')

@diaries_bp.route('/')
def get_all_diaries():
    stmt = db.select(Diary)
    diaries = db.session.scalars(stmt) #multiple scalars
    return diaries_schema.dump(diaries)

@diaries_bp.route('/<int:diary_id>')
def get_one_diary(diary_id):
    stmt = db.select(Diary).filter_by(diary_id=diary_id)
    diary = db.session.scalar(stmt) #single scalar
    if diary:
        return diary_schema.dump(diary)
    else:
        return {'error': f'Diary not found with id {diary_id}'}, 404
    
@diaries_bp.route('/', methods=['POST'])
@jwt_required()
def create_diary():
    body_data = request.get_json()
    diary = Diary(
        users_user_id=get_jwt_identity(),
        diary_title=body_data.get('diary_title')
    )
    db.session.add(diary)
    db.session.commit()
    return diary_schema.dump(diary), 201

@diaries_bp.route('/<int:diary_id>', methods=['DELETE'])
def delete_one_diary(diary_id):
    stmt = db.select(Diary).filter_by(diary_id=diary_id)
    diary = db.session.scalar(stmt)
    if diary:
        db.session.delete(diary)
        db.session.commit()
        return {'message': f'Diary: {diary.diary_title} deleted successfully'}
    else:
        return {'error': f'Diary not found with id {diary_id}'}, 404
    
@diaries_bp.route('/<int:diary_id>', methods=['PUT', 'PATCH'])
@jwt_required()
def update_one_card(diary_id):
    body_data = request.get_json()
    stmt = db.select(Diary).filter_by(diary_id=diary_id)
    diary = db.session.scalar(stmt)
    if diary:
        diary.diary_title = body_data.get('diary_title') or diary.diary_title
        db.session.commit()
        return diary_schema.dump(diary)
    else:
        return {'error': f'Diary not found with id {diary_id}'}, 404
