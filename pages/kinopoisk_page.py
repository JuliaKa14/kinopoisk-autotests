import allure

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class KinopoiskPage:
    """Страница Кинопоиска."""

    SEARCH_INPUT = (
        By.CSS_SELECTOR,
        "input[placeholder='Фильмы, сериалы, персоны']"
    )

    AD_CLOSE_BUTTON = (
        By.CSS_SELECTOR,
        "button[data-tid='CloseButton']"
    )

    MOVIE_CARD = (
        By.CSS_SELECTOR,
        "a[href='/film/535341/']"
    )

    MOVIE_TITLE = (
        By.CSS_SELECTOR,
        "span[data-tid='75209b22']"
    )

    MOVIE_RATING = (
        By.CSS_SELECTOR,
        "span.styles_ratingKpTop__8p7mM"
    )

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def close_ad(self) -> None:
        with allure.step("Закрыть рекламное окно"):
            try:
                buttons = self.driver.find_elements(
                    *self.AD_CLOSE_BUTTON
                )

                if buttons:
                    buttons[0].click()

            except Exception:
                pass

    def open(self) -> None:
        with allure.step("Открыть сайт Кинопоиска"):
            self.driver.get("https://www.kinopoisk.ru")
            self.close_ad()

    def search_movie(self, movie_name: str) -> None:
        with allure.step("Ввести название фильма"):

            search = self.wait.until(
                EC.element_to_be_clickable(self.SEARCH_INPUT)
            )

            search.send_keys(movie_name)
            search.submit()

    def check_movie_result(self, movie_name: str) -> WebElement:
        with allure.step("Проверить наличие фильма в результатах поиска"):
            return self.wait.until(
                EC.visibility_of_element_located(
                    (
                        By.XPATH,
                        f"//*[contains(text(),'{movie_name}')]"
                    )
                )
            )

    def is_movie_found(self, movie_name: str) -> bool:
        with allure.step("Проверить наличие фильма в результатах"):
            try:
                self.wait.until(
                    EC.visibility_of_element_located(
                        (
                            By.XPATH,
                            f"//*[contains(text(),'{movie_name}')]"
                        )
                    )
                )
                return True
            except Exception:
                return False

    def open_movie_card(self) -> None:
        with allure.step("Открыть карточку фильма"):
            movie = self.wait.until(
                EC.element_to_be_clickable(
                    self.MOVIE_CARD
                )
            )

            movie.click()

    def get_movie_title(self) -> WebElement:
        with allure.step("Получить название фильма"):
            return self.wait.until(
                EC.visibility_of_element_located(
                    self.MOVIE_TITLE
                )
            )

    def get_movie_rating(self) -> WebElement:
        with allure.step("Получить рейтинг фильма"):
            return self.wait.until(
                EC.visibility_of_element_located(
                    self.MOVIE_RATING
                )
            )
