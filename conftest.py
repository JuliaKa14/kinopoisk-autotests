import pytest

from api.movie_api import MovieAPI

@pytest.fixture
def movie_api():
    return MovieAPI()
