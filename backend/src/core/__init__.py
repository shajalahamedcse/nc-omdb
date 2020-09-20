from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_seeder import FlaskSeeder
from flask_jwt_extended import JWTManager
from src.core.config import Configuration



app= Flask(__name__)
seeder = FlaskSeeder()

CORS(app)
app.config.from_object(Configuration)

db = SQLAlchemy(app)

seeder.init_app(app, db)

jwt = JWTManager(app)

