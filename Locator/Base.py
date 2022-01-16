import allure

class Locator:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Assert elements")
    def assert_elements(first_element, second_element):
        try:
            assert first_element == second_element
            print("Assert: True")
        except:
            print("Assert: False")