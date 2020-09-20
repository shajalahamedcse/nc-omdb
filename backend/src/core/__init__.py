from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from src.core.config import Configuration

app= Flask(__name__)
CORS(app)
app.config.from_object(Configuration)

db = SQLAlchemy(app)