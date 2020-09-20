from flask import Blueprint, request
from flask_jwt_extended import jwt_required, current_user
from flask_restful import Api, Resource

from src.repository.search import MovieSearchRepository
from src.utils import ResponseGenerator

search_blueprint = Blueprint(name="searchbp", import_name=__name__, url_prefix="/api/v1/movie")
api = Api(app=search_blueprint)


class SearchMovie(Resource):
    method_decorators = [jwt_required]

    def get(self):
        mandatory_fields = ["q"]
        if any(request.args.get(item, default=None) is None for item in mandatory_fields):
            return ResponseGenerator.mandatory_field(fields=mandatory_fields)

        query = request.args.get("q", default=None, type=str)
        page = request.args.get("page", default=1, type=int)

        movies = MovieSearchRepository.search(search_query=query, page=page)
        return ResponseGenerator.generate_response(data=movies, code=200)
    
    
api.add_resource(SearchMovie, "/search")