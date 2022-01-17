import allure

class Locator:

    def __init__(self, driver):
        self.driver = driver

    def assert_elements(first_element, second_element):
        assert first_element == second_element