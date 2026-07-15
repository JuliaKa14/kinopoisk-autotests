import pytest


from typing import Generator

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager

from api.movie_api import MovieAPI


@pytest.fixture
def movie_api() -> MovieAPI:
    return MovieAPI()


@pytest.fixture
def driver() -> Generator[WebDriver, None, None]:
    driver = webdriver.Chrome(
        service=Service(
            ChromeDriverManager().install()
        )
    )

    driver.maximize_window()

    yield driver

    driver.quit()
