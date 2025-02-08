import logging
import os
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.logger = self.__config_logger()

    def __config_logger(self):
        logger = logging.getLogger(self.__class__.__name__)
        logger.setLevel(logging.INFO)

        if logger.hasHandlers():
            logger.handlers.clear()

        formatter = logging.Formatter(
            "%(asctime)s [%(levelname)s] %(name)s: %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )

        os.makedirs("logs", exist_ok=True)
        log_file = f"logs/{self.driver.test_name}.log"

        file_handler = logging.FileHandler(log_file, encoding="utf-8")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

        return logger

    def open(self, url: str):
        self.logger.info(f"Open page {url}")
        self.driver.get(url)

    def get_find_element(self, locator: str, timeout=5):
        self.logger.info(f"Looking for element {locator}")
        try:
            element = wait(self.driver, timeout, poll_frequency=1).until(EC.visibility_of_element_located(locator))
            self.logger.debug(f"Element found: {locator}")
            return element
        except Exception as e:
            self.logger.error(f"Error finding element {locator}: {e}")
            return None

    def click(self, locator: str, timeout=5):
        self.logger.info(f"Click on {locator}")
        try:
            wait(self.driver, timeout, poll_frequency=1).until(EC.element_to_be_clickable(locator)).click()
            self.logger.debug(f"Click successful: {locator}")
        except Exception as e:
            self.logger.error(f"Error clicking element {locator}: {e}")

    def check_element_visible(self, locator: str, timeout=5):
        self.logger.info(f"Checking if element is visible: {locator}")
        wait(self.driver, timeout, poll_frequency=1).until(EC.visibility_of_element_located(locator))

    def check_elements_visible(self, locators_list: list, timeout=5):
        self.logger.info(f"Checking visibility of elements: {locators_list}")
        for locator in locators_list:
            self.logger.info(f"Check element visible {locator}")
            wait(self.driver, timeout, poll_frequency=1).until(EC.visibility_of_element_located(locator))

    def check_element_not_visible(self, locator: str, timeout=5):
        self.logger.info(f"Checking if element is NOT visible: {locator}")
        try:
            return wait(self.driver, timeout=timeout, poll_frequency=1).until(EC.invisibility_of_element(locator))
        except Exception as e:
            self.logger.error(f"Error checking invisibility of element {locator}: {e}")
            return False

    def move_to_element(self, locator, timeout=5):
        try:
            self.logger.info(f"Moving cursor to element: {locator}")
            element = self.get_find_element(locator, timeout)
            actions = ActionChains(self.driver)
            actions.move_to_element(element).perform()
            self.logger.debug(f"Cursor moved to {locator}")
        except Exception as e:
            self.logger.info(f"Error moving cursor to element {locator}: {e}")

    def move_to_element_and_click(self, locator: str, timeout=5):
        try:
            self.logger.info(f"Moving cursor and clicking on element: {locator}")
            self.move_to_element(locator)
            element = wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
            element.click()
        except Exception as e:
            self.logger.info(f"Error click to element {locator}: {e}")

    def input(self, locator: str, data: str):
        self.logger.info(f"Typing '{data}' into {locator}")
        self.get_find_element(locator).send_keys(data)

    def switch_to_alert_and_accept(self):
        self.logger.info(f"Accept alert")
        try:
            alert = self.driver.switch_to.alert
            alert.accept()
            self.logger.debug("Alert accepted successfully")
        except Exception as e:
            self.logger.error(f"Error accepting alert: {e}")
