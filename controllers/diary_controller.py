from flask import Blueprint, request
from init import db
from models.diary import Diary, diaries_schema, diary_schema

diaries_bp = Blueprint('diaries', __name__, url_prefix='/diary')

@diaries_bp.route('/')
def get_all_diaries():
    stmt = db.select(Diary).order_by(Diary.diary_title.desc())
    diaries = db.session.scalars(stmt)
    return diaries_schema.dump(diaries)