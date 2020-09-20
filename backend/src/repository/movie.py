from typing import Dict, List, Union, Optional


from src.models.omdb import OMDBClient



class MovieRepository(object):
    omdb_client = OMDBClient()

    @staticmethod
    def get_movie_info(movie) -> Optional[Dict[str, Union[str, int, List, Dict]]]:
        
        movie_data = MovieRepository.omdb_client.get_full_movie_info(imdb_id=movie.imdb_id)
        return movie_data