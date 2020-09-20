from src.core import app
from src.core import jwt
from src.resource.user import user_blueprint
from src.models.user import User
from src.repository.user import UserRepository
from src.resource.search import search_blueprint
from src.utils import ResponseGenerator


@jwt.user_loader_callback_loader
def flask_jwt_user_loader_callback(identity) -> User:
    return UserRepository.get_by_id(id=identity)


@jwt.user_loader_error_loader
def flask_jwt_user_loader_error_callback(identity):
    return ResponseGenerator.not_found(msg="User::{} not found".format(identity))

@app.route("/")
def index():
    return {"mg":"working"}

app.register_blueprint(user_blueprint)
app.register_blueprint(search_blueprint)

if __name__=="__main__":
    app.run(debug=True,host="0.0.0.0",port=5000)