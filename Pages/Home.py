import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Home:

    def __init__(self, driver):
        self.driver = driver

        self._search_field = "text"
        self._button_images = "//a[@data-id = 'images']"
        self._suggest = "mini-suggest__popup.mini-suggest__popup_svg_yes.mini-suggest__popup_theme_tile.mini-suggest__popup_visible"

    def enter_keyword_in_search_field(self, keyword):
        self.driver.find_element(By.ID, self._search_field).is_displayed()
        self.driver.find_element(By.ID, self._search_field).send_keys(keyword)

    def check_suggest(self):
        self.driver.find_element(By.CLASS_NAME, self._suggest).is_displayed()

    def click_button_enter(self):
        self.driver.find_element(By.ID, self._search_field).send_keys(Keys.ENTER)

    def click_button_link_images(self):
        self.driver.find_element(By.XPATH, self._button_images).is_displayed()
        self.driver.find_element(By.XPATH, self._button_images).click()
