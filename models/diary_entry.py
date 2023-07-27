from init import db, ma
from marshmallow import fields
from datetime import datetime

class Diary_Entry(db.Model):
    __tablename__ = 'diary_entries'

    diaries_diary_id = db.Column(db.Integer, db.ForeignKey('diaries.diary_id'), primary_key=True, nullable=False)
    meals_meal_id = db.Column(db.Integer, db.ForeignKey('meals.meal_id'), primary_key=True, nullable=False)
    # health_analysis_ha_id = db.Column(db.Integer, db.ForeignKey('health_analysis.ha_id'), primary_key=True, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    diary = db.relationship('Diary', back_populates='diary_entries')
    meal = db.relationship('Meal', back_populates='diary_entries')

class Diary_EntrySchema(ma.Schema):
    diary = fields.Nested('DiarySchema', only=['title'])
    meal = fields.Nested('MealSchema', only=['meal_name', 'is_takeaway', 'kilojoules', 'notes'])

    class Meta:
        fields = ('diaries_diary_id', 'meals_meal_id', 'timestamp', 'diary', 'meal')
        #'health_analysis_ha_id'
        ordered = True

diary_entry_schema = Diary_EntrySchema()
diary_entries_schema = Diary_EntrySchema(many=True)