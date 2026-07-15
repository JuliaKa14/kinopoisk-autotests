import requests

from config import BASE_URL, API_KEY


class MovieAPI:
    """Класс для работы с API Кинопоиска."""

    def __init__(self):
        self.headers = {
            "X-API-KEY": API_KEY,
            "accept": "application/json"
        }

    def search_movie(self, query, page=1, limit=5):
        """Поиск фильма по названию."""
        response = requests.get(
            f"{BASE_URL}/v1.4/movie/search",
            headers=self.headers,
            params={
                "query": query,
                "page": page,
                "limit": limit
            }
        )
        return response

    def get_movie_by_id(self, movie_id):
        """Получение фильма по ID."""
        response = requests.get(
            f"{BASE_URL}/v1.4/movie/{movie_id}",
            headers=self.headers
        )
        return response

    def search_without_token(self, query):
        """Поиск фильма без API-ключа."""
        response = requests.get(
            f"{BASE_URL}/v1.4/movie/search",
            headers={
                "accept": "application/json"
            },
            params={
                "query": query
            }
        )
        return response

    def search_with_invalid_token(self, query):
        """Поиск фильма с неверным API-ключом."""
        response = requests.get(
            f"{BASE_URL}/v1.4/movie/search",
            headers={
                "X-API-KEY": "invalid_token",
                "accept": "application/json"
            },
            params={
                "query": query
            }
        )
        return response

    def get_movie_by_invalid_id(self, movie_id):
        """Получение фильма с несуществующим ID."""
        response = requests.get(
            f"{BASE_URL}/v1.4/movie/{movie_id}",
            headers=self.headers
        )
        return response
