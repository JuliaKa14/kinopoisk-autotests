import pytest
from api.movie_api import MovieAPI


@pytest.fixture
def movie_api():
    return MovieAPI()

import pytest

from api.movie_api import MovieAPI
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def movie_api():
    return MovieAPI()

@pytest.fixture
def driver():
    driver = webdriver.Chrome(
        service=Service(
            ChromeDriverManager().install()
        )
    )

    driver.maximize_window()

    yield driver

    driver.quit()