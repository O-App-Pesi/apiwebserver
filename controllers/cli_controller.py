from flask import Blueprint
from init import db, bcrypt
from models.user import User
from models.diary import Diary
from models.meal import Meal
from models.diary_entry import Diary_Entry
from datetime import date

db_commands = Blueprint('db', __name__)

@db_commands.cli.command('create')
def create_all():
    db.create_all()
    print('Tables Created')

@db_commands.cli.command('drop')
def drop_all():
    db.drop_all()
    print('Tables dropped')

@db_commands.cli.command('seed')
def seed_db():
    users = [
        User(
            email='user@user.com',
            password=bcrypt.generate_password_hash('user123').decode('utf-8')
        )
    ]
    db.session.add_all(users)

    diaries = [
        Diary(
            user = users[0],
            diary_title = "My First Diary"
        )
    ]

    db.session.add_all(diaries)

    meals = [
        Meal(
            user = users[0],
            meal_name = "Delicious Teriyaki",
            is_takeaway = True,
            kilojoules = 8000,
            notes = "made me fart"
        )
    ]

    db.session.add_all(meals)

    diary_entries = [
        Diary_Entry(
            diary = diaries[0],
            meal = meals[0]
        )
    ]

    db.session.add_all(diary_entries)
    db.session.commit()
