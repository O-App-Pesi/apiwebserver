from flask import Blueprint, request
from init import db
from models.diary_entry import DiaryEntry, diary_entry_schema, diary_entries_schema

diary_entry_bp = Blueprint('diary_entries', __name__, url_prefix='/diaryentry')

@diary_entry_bp.route('/')
def get_all_diary_entries():
    stmt = db.select(DiaryEntry)
    diary_entries = db.session.scalars(stmt)
    return diary_entries_schema.dump(diary_entries)