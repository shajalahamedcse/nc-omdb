import os
from src.utils import Generator

class FlaskConfig:
    APPLICATION_ROOT: str = "/api/v1"
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "DEV")
    SECRET_KEY: str = os.getenv("SECRET_KEY", Generator.random_string_generator(length=64, punctuation=False))
    
    
class Configuration:
    # application config
    APPLICATION_ROOT: str = FlaskConfig.APPLICATION_ROOT
    ENV: str = FlaskConfig.ENVIRONMENT
    DEBUG: bool = FlaskConfig.ENVIRONMENT == "DEV"
    SECRET_KEY: str = FlaskConfig.SECRET_KEY