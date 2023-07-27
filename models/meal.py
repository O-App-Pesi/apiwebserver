from init import db, ma
from marshmallow import fields

class Meal(db.Model):
    __tablename__ = "meals"

    meal_id = db.Column(db.Integer, primary_key=True)
    users_user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    meal_name = db.Column(db.String(100))
    is_takeaway = db.Column(db.Boolean, default=False)
    kilojoules = db.Column(db.Integer, nullable=False)
    notes = db.Column(db.String(255))

    user = db.relationship('User', back_populates='meals')
    diary_entries = db.relationship('DiaryEntry', back_populates='meal', cascade='all, delete')

class MealSchema(ma.Schema):
    user = fields.Nested('UserSchema', only=['email'])
    diary_entries = fields.List(fields.Nested('DiarySchema'), exclude=['diary'])
    class Meta:
        fields = ('meal_id', 'users_user_id', 'meal_name', 'is_takeaway', 'kilojoules', 'notes')
        ordered = True

meal_schema = MealSchema()
meals_schema = MealSchema(many=True)