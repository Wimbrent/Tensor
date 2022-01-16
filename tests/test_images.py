import time

import allure
import pytest
from allure_commons.types import AttachmentType

from Pages.Home import Home
from Pages.Imegas import Images
from Locator.Base import Locator


@pytest.mark.usefixtures('setup')
@pytest.mark.parametrize('Keyword', [(0)])
@allure.feature("Yandex Images")
@allure.severity(allure.severity_level.CRITICAL)
class TestImages:

    def test_images(self, Keyword):
        driver = self.driver

        yandex_page = Home(driver)
        yandex_images = Images(driver)
        locator = Locator

        print(f"Home url is: {driver.current_url}")
        with allure.step("get a screenshot of the link button to the Yandex images page"):
            allure.attach(driver.get_screenshot_as_png(), name="Images", attachment_type=AttachmentType.PNG)
        yandex_page.click_button_link_images()
        driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(2)
        print(f"Pictures url is: {driver.current_url}")
        time.sleep(2)
        yandex_images.get_text_image(Keyword)
        yandex_images.select_image_category(Keyword)
        yandex_images.get_text_from_search_field()
        locator.assert_elements(yandex_images.get_text_image(Keyword), yandex_images.get_text_from_search_field())
        time.sleep(3)
        with allure.step("Get screenshot of Yandex Images Pages"):
            allure.attach(driver.get_screenshot_as_png(), name="Yandex_Images_Page", attachment_type=AttachmentType.PNG)
        yandex_images.click_image(0)
        yandex_images.first_assert_image()
        yandex_images.click_button_next()
        yandex_images.click_button_previous()
        yandex_images.second_assert_image()
        locator.assert_elements(yandex_images.first_assert_image(), yandex_images.second_assert_image())