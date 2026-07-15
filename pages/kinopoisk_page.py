import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


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

    MOVIE_RESULT = (
        By.XPATH,
        "//*[contains(text(),'1+1')]"
    )

    MOVIE_CARD = (
        By.CSS_SELECTOR,
        "a[href*='/film/']"
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def close_ad(self):
        with allure.step("Закрыть рекламное окно"):
            try:
                close_button = WebDriverWait(
                    self.driver,
                    5
                ).until(
                    EC.element_to_be_clickable(
                        self.AD_CLOSE_BUTTON
                    )
                )

                close_button.click()

            except TimeoutException:
                pass


    def open(self):
        with allure.step("Открыть сайт Кинопоиска"):
            self.driver.get("https://www.kinopoisk.ru")
            self.close_ad()

    def search_movie(self, movie_name):
        with allure.step("Ввести название фильма"):
            self.close_ad()

            search = self.wait.until(
                EC.element_to_be_clickable(self.SEARCH_INPUT)
            )
            search.send_keys(movie_name)
            search.submit()

    def check_movie_result(self, movie_name):
        with allure.step("Проверить наличие фильма в результатах поиска"):
            return self.wait.until(
                EC.visibility_of_element_located(
                (
                    By.XPATH,
                    f"//*[contains(text(),'{movie_name}')]"
                )
            )
        )

    def is_movie_found(self, movie_name):
        with allure.step("Проверить наличие фильма в результатах"):
            return self.wait.until(
                EC.visibility_of_element_located(
                (
                    By.XPATH,
                    f"//*[contains(text(),'{movie_name}')]"
                )
            )
        )

    def open_movie_card(self):
        with allure.step("Открыть карточку фильма"):
            movie = self.wait.until(
                EC.element_to_be_clickable(
                self.MOVIE_CARD
            )
        )

        movie.click()

