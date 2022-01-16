import allure
from selenium.webdriver.common.by import By


class Images:
    def __init__(self, driver):
        self.driver = driver

        self._image_categories = "//*[@class = 'PopularRequestList']/div"
        self._get_text_from_image = "PopularRequestList-SearchText"
        self._search_field = "text"
        self._image = "serp-item__preview"
        self._image_container = "MMImage-Origin"
        self._button_next = "//div[@class = 'MediaViewer-LayoutScene MediaViewer_theme_fiji-LayoutScene']/div[4]"
        self._button_previous = "//div[@class = 'MediaViewer-LayoutScene MediaViewer_theme_fiji-LayoutScene']/div[1]"

    @allure.step("Get text from images category")
    def get_text_image(self, select):
        elements = self.driver.find_elements(By.XPATH, self._image_categories)
        elements[select].text

    @allure.step("Select images category")
    def select_image_category(self, select):
        elements = self.driver.find_elements(By.XPATH, self._image_categories)
        elements[select].click()

    @allure.step("Get text from search field")
    def get_text_from_search_field(self):
        field = self.driver.find_element(By.NAME, self._search_field)
        field.get_attribute('value')

    @allure.step("Click on the selected image")
    def click_image(self, select):
        elements = self.driver.find_elements(By.CLASS_NAME, self._image)
        elements[select].click()

    @allure.step("Click button next")
    def click_button_next(self):
        self.driver.find_element(By.XPATH, self._button_next).click()

    @allure.step("Click button previous")
    def click_button_previous(self):
        self.driver.find_element(By.XPATH, self._button_previous).click()

    @allure.step("Get text from image")
    def first_assert_image(self):
        self.driver.find_element(By.CLASS_NAME, self._image_container).get_attribute('src')

    @allure.step("Get text from image")
    def second_assert_image(self):
        self.driver.find_element(By.CLASS_NAME, self._image_container).get_attribute('src')