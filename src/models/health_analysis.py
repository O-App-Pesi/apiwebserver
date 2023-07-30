from init import db, ma
from marshmallow import fields
from marshmallow.validate import Length, And, Regexp

class HealthAnalysis(db.Model):
    __tablename__ = 'health_analysis'

    ha_id = db.Column(db.Integer, primary_key=True)
    physical_change = db.Column(db.String(255))
    mood_change = db.Column(db.String(255))

    diary_entries = db.relationship('DiaryEntry', back_populates='health_analysis', cascade='all, delete')

class HealthAnalysisSchema(ma.Schema):
    diary_entries = fields.List(fields.Nested('DiaryEntrySchema', exclude=['diary_entries']))

    physical_change = fields.String(required=True, validate=And(
        Length(min=4, error='physical change must be at least 4 characters long')))
    mood_change = fields.String(required=True, validate=And(
        Length(min=4, error='mood change must be at least 4 characters long')))
    class Meta:
        fields = ('ha_id', 'physical_change', 'mood_change')

health_analysis_schema = HealthAnalysisSchema()
ha_schema = HealthAnalysisSchema(many=True)