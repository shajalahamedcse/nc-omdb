from flask import Flask
from src.core.config import Configuration

app= Flask(__name__)

app.config.from_object(Configuration)