from flask import Blueprint, request
from flask_jwt_extended import jwt_required, current_user
from src.utils import ResponseGenerator
from src.repository.user import UserRepository
from flask_restful import Api,Resource

user_blueprint = Blueprint(name="userbp", import_name=__name__, url_prefix="/api/v1")
api = Api(app=user_blueprint)

class UserLogin(Resource):
 

    def post(self):
        data = request.get_json()

        email = data["email"]
        password = data["password"]

        user = UserRepository.get_by_email(email=email)
        if not user:
            return ResponseGenerator.not_found(msg="user not found")

        if not user.check_password(password=password):
            return ResponseGenerator.forbidden(msg="email/password combination is invalid")

        access_token = UserRepository.create_user_access_token(user=user)
        return ResponseGenerator.generate_response({
            "access_token": access_token
        }, code=200)
        
class UserAuthenticate(Resource):
    
    @jwt_required
    def get(self):
        return ResponseGenerator.generate_response(current_user.json, code=200)
        
api.add_resource(UserLogin, "/login")
api.add_resource(UserAuthenticate, "/authenticate")