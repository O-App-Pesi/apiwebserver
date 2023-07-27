from init import db, ma
from marshmallow import fields

class Diary(db.Model):
    __tablename__ = "diaries"

    diary_id = db.Column(db.Integer, primary_key=True)
    users_user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    diary_title = db.Column(db.String(100))

    user = db.relationship('User', back_populates='diaries')
    diary_entries = db.relationship('DiaryEntry', back_populates='diary', cascade='all, delete')

class DiarySchema(ma.Schema):
    user = fields.Nested('UserSchema', only=['email'])
    diary_entries = fields.List(fields.Nested('DiarySchema'), exclude=['diary'])
    class Meta:
        fields = ('diary_id', 'users_user_id', 'diary_title')
        ordered = True

diary_schema = DiarySchema()
diaries_schema = DiarySchema(many=True)