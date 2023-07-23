from init import db, ma

class User(db.model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(50), nullable=False)

class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'email', 'password')

user_schema = UserSchema(exclude=['password'])
users_schema = UserSchema(many=True, exclude=['password'])
