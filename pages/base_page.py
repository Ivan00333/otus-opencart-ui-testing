import logging
import os
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.__config_logger()

    def __config_logger(self, to_file=True):
        self.logger = logging.getLogger(type(self).__name__)
        os.makedirs("logs", exist_ok=True)
        if to_file:
            self.logger.addHandler(logging.FileHandler(f"logs/{self.driver.test_name}.log"))
        self.logger.setLevel(level=self.driver.log_level)

    def open(self, url: str):
        self.logger.info(f"Open {url}")
        self.driver.get(url)

    def get_find_element(self, locator: str, timeout=5):
        self.logger.info(f"Get element {locator}")
        return wait(self.driver, timeout, poll_frequency=1).until(EC.visibility_of_element_located(locator))

    def click(self, locator: str, timeout=5):
        self.logger.info(f"Click on {locator}")
        wait(self.driver, timeout, poll_frequency=1).until(EC.element_to_be_clickable(locator)).click()

    def check_element_visible(self, locator: str, timeout=5):
        self.logger.info(f"Check visible element {locator}")
        wait(self.driver, timeout, poll_frequency=1).until(EC.visibility_of_element_located(locator))

    def check_elements_visible(self, locators_list: list, timeout=5):
        self.logger.info(f"Check visible elements in list {locators_list}")
        for locator in locators_list:
            self.logger.info(f"Check element visible {locator}")
            wait(self.driver, timeout, poll_frequency=1).until(EC.visibility_of_element_located(locator))

    def check_element_not_visible(self, locator: str, timeout=5):
        try:
            self.logger.info(f"Check invisible element {locator}")
            wait(self.driver, timeout=timeout, poll_frequency=1).until(EC.invisibility_of_element(locator))
        except Exception as e:
            self.logger.info(f"Error check element {locator}: {e}")

    def move_to_element(self, locator, timeout=5):
        try:
            self.logger.info(f"Move to element {locator}")
            element = self.get_find_element(locator, timeout)
            actions = ActionChains(self.driver)
            actions.move_to_element(element).perform()
        except Exception as e:
            self.logger.info("Error moving to element")

    def move_to_element_and_click(self, locator: str, timeout=5):
        try:
            self.logger.info(f"Click to element {locator}")
            self.move_to_element(locator)
            element = wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
            element.click()
        except Exception as e:
            self.logger.info(f"Error click to element: {e}")

    def input(self, locator: str, data: str):
        self.logger.info(f"Input {data} in {locator}")
        self.get_find_element(locator).send_keys(data)

    def switch_to_alert_and_accept(self):
        self.logger.info(f"Accept alert")
        alert = self.driver.switch_to.alert
        alert.accept()
