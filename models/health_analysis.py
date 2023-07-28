from init import db, ma
from marshmallow import fields

class HealthAnalysis(db.Model):
    __tablename__ = 'health_analysis'

    ha_id = db.Column(db.Integer, primary_key=True)
    physical_change = db.Column(db.String(255), nullable=False)
    mood_change = db.Column(db.String(255), nullable=False)

    diary_entries = db.relationship('DiaryEntry', back_populates='health_analysis', cascade='all, delete')

class HealthAnalysisSchema(ma.Schema):
    diary_entries = fields.List(fields.Nested('DiaryEntrySchema', exclude=['diary_entries']))
    class Meta:
        fields = ('ha_id', 'physical_change', 'mood_change')

health_analysis_schema = HealthAnalysisSchema()
ha_schema = HealthAnalysisSchema(many=True)