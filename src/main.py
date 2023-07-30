from flask import Flask
import os
from init import db, ma, bcrypt, jwt
from controllers.cli_controller import db_commands
from controllers.auth_controller import auth_bp
from controllers.diary_controller import diaries_bp
from controllers.meal_controller import meals_bp
from controllers.health_analysis_controller import health_analysis_bp
from controllers.diary_entry_controller import diary_entry_bp

def create_app():
    app = Flask(__name__)

    app.json.sort_keys = False
                                        
    app.config["SQLALCHEMY_DATABASE_URI"]=os.environ.get("DATABASE_URL")
    app.config["JWT_SECRET_KEY"]=os.environ.get("JWT_SECRET_KEY")

    db.init_app(app)
    ma.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    app.register_blueprint(db_commands)
    app.register_blueprint(auth_bp)
    app.register_blueprint(diaries_bp)
    app.register_blueprint(meals_bp)
    app.register_blueprint(diary_entry_bp)
    app.register_blueprint(health_analysis_bp)

    return app