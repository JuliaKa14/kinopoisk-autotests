import allure

@allure.title("Поиск фильма по названию")
def test_search_movie(movie_api):

    with allure.step("Отправить запрос на поиск фильма"):
        response = movie_api.search_movie("1+1")

    with allure.step("Проверить статус ответа"):
        assert response.status_code == 200

    with allure.step("Проверить наличие результатов поиска"):
        assert len(response.json()["docs"]) > 0


@allure.title("Получение фильма по ID")
def test_get_movie_by_id(movie_api):

    with allure.step("Отправить запрос на получение фильма"):
        response = movie_api.get_movie_by_id(535341)

    with allure.step("Проверить статус ответа"):
        assert response.status_code == 200

    with allure.step("Проверить наличие ID фильма в ответе"):
        assert response.json()["id"] == 535341

@allure.title("Проверка ограничения количества результатов поиска")
def test_search_movie_limit(movie_api):

    with allure.step("Отправить запрос с limit=5"):
        response = movie_api.search_movie(
            "аватар",
            limit=5
        )

    with allure.step("Проверить статус ответа"):
        assert response.status_code == 200

    with allure.step("Проверить количество результатов"):
        assert len(response.json()["docs"]) <= 5

@allure.title("Поиск фильма без API-ключа")
def test_search_movie_without_token(movie_api):

    with allure.step("Отправить запрос без токена"):
        response = movie_api.search_without_token("1+1")

    with allure.step("Проверить статус 401"):
        assert response.status_code == 401

    with allure.step("Проверить сообщение об ошибке"):
        assert response.json()["error"] == "Unauthorized"

