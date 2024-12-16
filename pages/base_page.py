
import logging
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url : str):
        self.driver.get(url)

    def get_find_element(self, locator: str, timeout=5):
        return wait(self.driver, timeout, poll_frequency=1).until(EC.visibility_of_element_located(locator))

    def click(self, locator: str, timeout=5):
        wait(self.driver, timeout, poll_frequency=1).until(EC.element_to_be_clickable(locator)).click()
    
    def check_element_visible(self, locator: str, timeout=5):
        wait(self.driver, timeout, poll_frequency=1).until(EC.visibility_of_element_located(locator))

    def check_elements_visible(self, locators_list: list, timeout=5):
        for locator in locators_list:
            wait(self.driver, timeout, poll_frequency=1).until(EC.visibility_of_element_located(locator))

    def move_to_element(self, locator, timeout=5):
        try:
            element = self.get_find_element(locator, timeout)
            actions = ActionChains(self.driver)
            actions.move_to_element(element).perform()
        except Exception as e:
            print(f"Error moving to element")

    def move_to_element_and_click(self, locator: str, timeout=5):
        try:
            self.move_to_element(locator)
            element = wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
            element.click()
        except Exception as e:
            print(f"Error click to element: {e}")

    def input(self, locator: str, data: str):
        self.get_find_element(locator).send_keys(data)


