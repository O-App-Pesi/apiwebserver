from flask import Blueprint, request
from init import db
from models.diary_entry import Diary_Entry, diary_entry_schema, diary_entries_schema

diary_entry_bp = Blueprint('diary_entries', __name__, url_prefix='/diaryentry')

@diary_entry_bp.route('/')
def get_all_meals():
    stmt = db.select(Diary_Entry).order_by(Diary_Entry.timestamp)
    diaries = db.session.scalars(stmt)
    return diary_entry_schema.dump(diaries)