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

        imagespage_url = "https://yandex.ru/images/?utm_source=main_stripe_big"

        with allure.step("Проверить наличие кнопки Картинки"):
            yandex_page.checkout_images_button()
        with allure.step("Нажать на кнопку Картинки"):
            yandex_page.click_button_link_images()
        # Переключить драйвер на новую вкладку браузера
        driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(2)
        with allure.step("Проверить url страницы"):
            locator.assert_elements(driver.current_url, imagespage_url)
        time.sleep(2)
        with allure.step("Получить название категории"):
            yandex_images.get_text_image(Keyword)
        with allure.step("Нажать на первую категорию изображения"):
            yandex_images.select_image_category(Keyword)
        with allure.step("Получить текст из поля поиска"):
            yandex_images.get_text_from_search_field()
        with allure.step("Сравнить название категории с текстом из поля поиска"):
            locator.assert_elements(yandex_images.get_text_image(Keyword), yandex_images.get_text_from_search_field())
        time.sleep(3)
        with allure.step("Нажать на картинку"):
            yandex_images.click_image(Keyword)
        with allure.step("Получить текст из названия картинки"):
            yandex_images.first_assert_image()
        with allure.step("Нажать кнопку Следующее"):
            yandex_images.click_button_next()
        with allure.step("Нажать кнопку Предыдущее"):
            yandex_images.click_button_previous()
        with allure.step("Получить текст из названия картинки"):
            yandex_images.second_assert_image()
        with allure.step("Сравнить текст"):
            locator.assert_elements(yandex_images.first_assert_image(), yandex_images.second_assert_image())