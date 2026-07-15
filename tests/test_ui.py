import allure

from pages.kinopoisk_page import KinopoiskPage


@allure.title("Поиск фильма через сайт Кинопоиск")
def test_search_movie_ui(driver):

    page = KinopoiskPage(driver)

    page.open()
    page.search_movie("1+1")

    with allure.step("Проверить результат поиска"):
        assert page.check_movie_result("1+1").is_displayed()


@allure.title("Проверка результата поиска фильма")
def test_movie_search_result(driver):

    page = KinopoiskPage(driver)

    page.open()
    page.search_movie("1+1")

    result = page.is_movie_found("1+1")

    assert result.is_displayed()


@allure.title("Открытие карточки фильма")
def test_open_movie_card(driver):

    page = KinopoiskPage(driver)

    page.open()
    page.search_movie("1+1")
    page.open_movie_card()

    with allure.step("Проверить, что открылась страница фильма"):
        assert "film" in driver.current_url

