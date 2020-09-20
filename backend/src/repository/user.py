from typing import List, Dict, Union, Optional
from flask_jwt_extended import create_access_token, create_refresh_token
from src.models.user import User

class UserRepository:
    @staticmethod
    def get_all() -> List[User]:
        return User.query.all()
    
    @staticmethod
    def get_by_id(id: int) -> User:
        return User.query.get(id)

    @staticmethod
    def get_by_email(email: str) -> User:
        return User.query.filter(
            User.email == email
        ).first()
        

    @staticmethod
    def create_user_access_token(user: User) -> str:
        return create_access_token(identity=user.id)

    @staticmethod
    def create_user_refresh_token(user: User) -> str:
        return create_refresh_token(identity=user.id)