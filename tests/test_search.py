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

        yandex_page.enter_keyword_in_search_field(keyword)
        time.sleep(3)
        yandex_page.check_suggest()
        with allure.step("Get screenshot of suggest element"):
            allure.attach(driver.get_screenshot_as_png(), name="Suggest", attachment_type=AttachmentType.PNG)
        yandex_page.click_button_enter()
        time.sleep(2)
        with allure.step("Get screenshot of result"):
            allure.attach(driver.get_screenshot_as_png(), name="Search_Result", attachment_type=AttachmentType.PNG)