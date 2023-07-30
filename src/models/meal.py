from init import db, ma
from marshmallow import fields
from marshmallow.validate import Length, And, Regexp, OneOf

VALID_BOOLEANS = (True, False)

class Meal(db.Model):
    __tablename__ = "meals"

    meal_id = db.Column(db.Integer, primary_key=True)
    users_user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    meal_name = db.Column(db.String(100))
    is_takeaway = db.Column(db.Boolean, default=False)
    kilojoules = db.Column(db.Integer)
    notes = db.Column(db.String(255))

    user = db.relationship('User', back_populates='meals')
    diary_entries = db.relationship('DiaryEntry', back_populates='meal', cascade='all, delete')

class MealSchema(ma.Schema):
    user = fields.Nested('UserSchema', only=['email'])
    diary_entries = fields.List(fields.Nested('DiarySchema'), exclude=['diary'])

    meal_name = fields.String(required=True, validate=And(
        Length(min=1, error='Meal Name must be at least 1 characters long'),
        Regexp('^[a-zA-Z0-9 ]+$', error='Only letters, spaces and numbers are allowed')
    ))
    notes = fields.String(required=True, validate=And(
        Length(min=5, error='Notes must have at least 5 characters')))
    is_takeaway = fields.Boolean()
    kilojoules = fields.Integer()
    class Meta:
        fields = ('meal_id', 'users_user_id', 'meal_name', 'is_takeaway', 'kilojoules', 'notes')
        ordered = True

meal_schema = MealSchema()
meals_schema = MealSchema(many=True)