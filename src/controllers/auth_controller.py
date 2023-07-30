from flask import Blueprint, request
from init import db, bcrypt
from models.user import User, user_schema, users_schema
from flask_jwt_extended import create_access_token, jwt_required
from sqlalchemy.exc import IntegrityError
from psycopg2 import errorcodes
from datetime import timedelta

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

#GET query, retrieves user entity from the database with matching user_id
#User must be logged in, action authenticated by jwt_required
@auth_bp.route('/<int:user_id>')
@jwt_required()
def get_user(user_id):
    stmt = db.select(User).filter_by(user_id=user_id)
    user = db.session.scalar(stmt) #single scalar
    if user:
        return user_schema.dump(user)
    else:
        return {'error': f'User not found'}, 404

#POST query, adds a new entity to the database from input data
#throws an error if the email is not unique or if the column is not nullable
@auth_bp.route('/register', methods=['POST'])
def auth_register():
    try:
        body_data = request.get_json()

        user = User()
        user.email = body_data.get('email')
        if body_data.get('password'):
            user.password = bcrypt.generate_password_hash(body_data.get('password')).decode('utf-8')

        db.session.add(user)

        db.session.commit()

        return user_schema.dump(user), 201
    except IntegrityError as err:
        if err.orig.pgcode == errorcodes.UNIQUE_VIOLATION:
            return {'error': 'Email address already in use'}, 409
        if err.orig.pgcode == errorcodes.NOT_NULL_VIOLATION:
            return {'error': f'The {err.orig.diag.column_name} is required'}, 409

#POST query, matches a user in the database and logs them in        
@auth_bp.route('/login', methods=['POST'])
def auth_login():
    body_data = request.get_json()

    stmt = db.select(User).filter_by(email=body_data.get('email'))
    user = db.session.scalar(stmt)

    if user and bcrypt.check_password_hash(user.password, body_data.get('password')):
        token = create_access_token(identity=str(user.user_id), expires_delta=timedelta(days=1))
        return { 'email': user.email, 'token': token }
    else:
        return { 'error': 'Invalid email or password' }, 401
    
#PUT/PATCH query, updates an entity in the user table
#User must be logged in, action authenticated by jwt_required
@auth_bp.route('/update/<int:user_id>', methods=['PUT', 'PATCH'])
@jwt_required()
def auth_update_user(user_id):
    try:
        body_data = request.get_json()

        stmt = db.select(User).filter_by(user_id=user_id)
        user = db.session.scalar(stmt)
        if user:
            if body_data.get('password'):
                user.password = bcrypt.generate_password_hash(body_data.get('password')).decode('utf-8') or user.password
            user.email = body_data.get('email') or user.email
        db.session.add(user)

        db.session.commit()

        return user_schema.dump(user), 201
    except IntegrityError as err:
        if err.orig.pgcode == errorcodes.UNIQUE_VIOLATION:
            return {'error': 'Email address already in use'}, 409
        if err.orig.pgcode == errorcodes.NOT_NULL_VIOLATION:
            return {'error': f'The {err.orig.diag.column} is required'}, 409

#DELETE query, deletes an entity from the user table based on user_id
#User must be logged in, action authenticated by jwt_required
@auth_bp.route('/<int:user_id>', methods=['DELETE'])
@jwt_required()
def delete_user(user_id):
    stmt = db.select(User).filter_by(user_id=user_id)
    user = db.session.scalar(stmt)
    if user:
        db.session.delete(user)
        db.session.commit()
        return {'message': f'User with email: {user.email} deleted successfully'}
    else:
        return {'error': f'User not found with specified email'}, 404