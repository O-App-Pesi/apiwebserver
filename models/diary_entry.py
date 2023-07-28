from init import db, ma
from marshmallow import fields
from datetime import datetime

class DiaryEntry(db.Model):
    __tablename__ = 'diary_entries'

    diaries_diary_id = db.Column(db.Integer, db.ForeignKey('diaries.diary_id'), primary_key=True, nullable=False)
    meals_meal_id = db.Column(db.Integer, db.ForeignKey('meals.meal_id'), primary_key=True, nullable=False)
    health_analysis_ha_id = db.Column(db.Integer, db.ForeignKey('health_analysis.ha_id'), primary_key=True, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    diary = db.relationship('Diary', back_populates='diary_entries', uselist=False)
    meal = db.relationship('Meal', back_populates='diary_entries', uselist=False)
    health_analysis = db.relationship('HealthAnalysis', back_populates='diary_entries', uselist=False)

class DiaryEntrySchema(ma.Schema):
    diary = fields.Nested('DiarySchema', exclude=['users_user_id', 'diary_id'])
    meal = fields.Nested('MealSchema', only=['meal_name', 'is_takeaway', 'kilojoules', 'notes'])
    health_analysis = fields.Nested('HealthAnalysisSchema')
    
    class Meta:
        fields = ('diaries_diary_id', 'meals_meal_id', 'health_analysis_ha_id' 'timestamp', 'diary', 'meal', 'health_analysis')
        ordered = True

diary_entry_schema = DiaryEntrySchema()
diary_entries_schema = DiaryEntrySchema(many=True)