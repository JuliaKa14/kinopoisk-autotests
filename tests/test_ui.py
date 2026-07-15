import allure
import pytest

from selenium.webdriver.chrome.webdriver import WebDriver

from pages.kinopoisk_page import KinopoiskPage


@pytest.mark.ui
@allure.title("Поиск фильма через сайт Кинопоиск")
@allure.story("Поиск фильма")
def test_search_movie_ui(driver: WebDriver) -> None:

    page = KinopoiskPage(driver)

    with allure.step("Открыть сайт Кинопоиска"):
        page.open()

    with allure.step("Выполнить поиск фильма 1+1"):
        page.search_movie("1+1")

    with allure.step("Проверить результат поиска"):
        assert page.check_movie_result("1+1").is_displayed()


@pytest.mark.ui
@allure.title("Проверка результата поиска фильма")
@allure.story("Поиск фильма")
def test_movie_search_result(driver: WebDriver) -> None:

    page = KinopoiskPage(driver)

    with allure.step("Открыть сайт Кинопоиска"):
        page.open()

    with allure.step("Выполнить поиск фильма 1+1"):
        page.search_movie("1+1")

    with allure.step("Проверить, что фильм найден"):
        assert page.is_movie_found("1+1")


@pytest.mark.ui
@allure.title("Открытие карточки фильма")
@allure.story("Карточка фильма")
def test_open_movie_card(driver: WebDriver) -> None:

    page = KinopoiskPage(driver)

    with allure.step("Открыть сайт Кинопоиска"):
        page.open()

    with allure.step("Выполнить поиск фильма 1+1"):
        page.search_movie("1+1")

    with allure.step("Открыть карточку фильма"):
        page.open_movie_card()

    with allure.step("Проверить, что открылась страница фильма"):
        assert "film" in driver.current_url


@pytest.mark.ui
@allure.title("Проверка названия фильма")
@allure.story("Карточка фильма")
def test_movie_title(driver: WebDriver) -> None:

    page = KinopoiskPage(driver)

    with allure.step("Открыть сайт Кинопоиска"):
        page.open()

    with allure.step("Выполнить поиск фильма 1+1"):
        page.search_movie("1+1")

    with allure.step("Открыть карточку фильма"):
        page.open_movie_card()

    with allure.step("Проверить название фильма"):
        assert "1+1" in page.get_movie_title().text


@pytest.mark.ui
@allure.title("Проверка отображения рейтинга фильма")
@allure.story("Карточка фильма")
def test_movie_rating(driver: WebDriver) -> None:

    page = KinopoiskPage(driver)

    with allure.step("Открыть сайт Кинопоиска"):
        page.open()

    with allure.step("Выполнить поиск фильма 1+1"):
        page.search_movie("1+1")

    with allure.step("Открыть карточку фильма"):
        page.open_movie_card()

    with allure.step("Проверить наличие рейтинга"):
        assert page.get_movie_rating().text != ""
