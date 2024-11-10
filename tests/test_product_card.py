import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestCatalogPage:
    URI_PRODUCT_CARD = '/en-gb/product/tablet/samsung-galaxy-tab-10-1'

    PRODUCT_IMAGE_LOCATOR = (By.XPATH, "//*[@class='image magnific-popup']")
    ADD_TO_CART_BUTTON_LOCATOR = (By.XPATH, "//*[text()='Add to Cart']")
    PRODUCT_NAME_LOCATOR = (By.XPATH, "//div/h1[text()='Samsung Galaxy Tab 10.1']")
    PRODUCT_PRICE_LOCATOR = (By.XPATH, "//*[@class='price-new']")
    PRODUCT_DESCRIPTION_LOCATOR = (By.XPATH, "//*[@class='tab-content']")

    locators_list = [
        PRODUCT_NAME_LOCATOR,
        ADD_TO_CART_BUTTON_LOCATOR,
        PRODUCT_NAME_LOCATOR,
        PRODUCT_PRICE_LOCATOR,
        PRODUCT_DESCRIPTION_LOCATOR
    ]

    def open_product_card_page(self, browser):
        browser.get(f"{browser.base_url}{self.URI_PRODUCT_CARD}")

    def check_element_visible(self, browser, locator):
        WebDriverWait(browser, 10, poll_frequency=1).until(EC.visibility_of_element_located(locator))

    @pytest.mark.parametrize("locator", locators_list)
    def test_check_visible_product_card_elements(self, browser, locator):
        self.open_product_card_page(browser)
        self.check_element_visible(browser, locator)
