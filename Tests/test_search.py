import time
import pytest
import allure

from Pages.Home import Home
from allure_commons.types import AttachmentType


@pytest.mark.usefixtures('setup')
@pytest.mark.parametrize('keyword', [('Тензор')])
@allure.feature("Yandex search and result")
@allure.severity(allure.severity_level.CRITICAL)
class TestSearchField:
    def test_search(self, keyword):

        driver = self.driver
        yandex_page = Home(driver)

        with allure.step("Проверить наличие поля поиска"):
            yandex_page.checkout_search_field()
        with allure.step("Ввести ключевое слово для поиска"):
            yandex_page.enter_keyword_in_search_field(keyword)
        time.sleep(3)
        with allure.step("Проверить наличие поля подсказки"):
            yandex_page.check_suggest()
        with allure.step("Нажать кнопку ввода"):
            yandex_page.click_button_enter()
        time.sleep(2)
        with allure.step("Сделать скриншот с результатом поиска"):
            allure.attach(driver.get_screenshot_as_png(), name="Search_Result", attachment_type=AttachmentType.PNG)