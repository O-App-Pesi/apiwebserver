from init import db, ma
from marshmallow import fields

class User(db.Model):
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)

    diaries = db.relationship('Diary', back_populates='user', cascade='all, delete')
    meals = db.relationship('Meal', back_populates='user', cascade='all, delete')

class UserSchema(ma.Schema):
    diaries = fields.List(fields.Nested('DiarySchema', exclude=['user']))
    meals = fields.List(fields.Nested('MealSchema', exclude=['user']))
    class Meta:
        fields = ('user_id', 'email', 'password', 'diaries')

user_schema = UserSchema(exclude=['password'])
users_schema = UserSchema(many=True, exclude=['password'])
