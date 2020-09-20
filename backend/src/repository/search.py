
from typing import List, Dict, Union

from src.models.search import MovieSearch


class MovieSearchRepository:
    search_client = MovieSearch()

    @staticmethod
    def search(search_query: str, page: int = 1) -> List[Dict[str, Union[str, int, List, Dict]]]:
        return MovieSearchRepository.search_client.search(search_query=search_query, page=page)