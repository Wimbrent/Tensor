import time

import pytest
from selenium import webdriver


@pytest.fixture
def get_webdriver():
    driver = webdriver.Firefox(executable_path="/Users/wimbrent/PycharmProjects/Tensor/Drivers/geckodriver")
    return driver


@pytest.fixture(scope='function')
def setup(request, get_webdriver):
    driver = get_webdriver
    driver.fullscreen_window()
    url = 'https://yandex.ru/'
    if request.cls is not None:
        request.cls.driver = driver
    driver.get(url)
    yield driver
    time.sleep(3)
    driver.quit()