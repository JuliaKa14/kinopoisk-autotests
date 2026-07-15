import pytest
import allure


@pytest.mark.api
@allure.title("Поиск фильма по названию")
def test_search_movie(movie_api) -> None:

    with allure.step("Отправить запрос на поиск фильма"):
        response = movie_api.search_movie("1+1")

    with allure.step("Проверить статус ответа"):
        assert response.status_code == 200

    with allure.step("Проверить наличие результатов поиска"):
        assert len(response.json()["docs"]) > 0


@pytest.mark.api
@allure.title("Получение фильма по ID")
def test_get_movie_by_id(movie_api) -> None:

    with allure.step("Отправить запрос на получение фильма"):
        response = movie_api.get_movie_by_id(535341)

    with allure.step("Проверить статус ответа"):
        assert response.status_code == 200

    with allure.step("Проверить наличие ID фильма в ответе"):
        assert response.json()["id"] == 535341


@pytest.mark.api
@allure.title("Проверка ограничения количества результатов поиска")
def test_search_movie_limit(movie_api) -> None:

    with allure.step("Отправить запрос с limit=5"):
        response = movie_api.search_movie(
            "аватар",
            limit=5
        )

    with allure.step("Проверить статус ответа"):
        assert response.status_code == 200

    with allure.step("Проверить количество результатов"):
        assert len(response.json()["docs"]) <= 5


@pytest.mark.api
@allure.title("Поиск фильма без API-ключа")
def test_search_movie_without_token(movie_api) -> None:

    with allure.step("Отправить запрос без токена"):
        response = movie_api.search_without_token("1+1")

    with allure.step("Проверить статус 401"):
        assert response.status_code == 401

    with allure.step("Проверить сообщение об ошибке"):
        assert response.json()["error"] == "Unauthorized"


@pytest.mark.api
@allure.title("Поиск фильма с неверным API-ключом")
def test_search_movie_with_invalid_token(movie_api) -> None:

    with allure.step("Отправить запрос с неверным токеном"):
        response = movie_api.search_with_invalid_token("1+1")

    with allure.step("Проверить статус ответа"):
        assert response.status_code == 401

    with allure.step("Проверить сообщение об ошибке"):
        assert response.json()["error"] == "Unauthorized"


@pytest.mark.api
@allure.title("Получение фильма по несуществующему ID")
def test_get_movie_by_invalid_id(movie_api) -> None:

    with allure.step("Отправить запрос с несуществующим ID"):
        response = movie_api.get_movie_by_invalid_id(999999999)

    with allure.step("Проверить статус ответа"):
        assert response.status_code in [400, 404]
