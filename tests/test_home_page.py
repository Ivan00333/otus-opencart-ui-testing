import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestHomePage:
    OPENCART_LOGO_LOCATOR = (By.XPATH, "//img[contains(@src, 'opencart-logo.png')]")
    SEARCH_LOCATOR = (By.XPATH, "//input[@name='search']")
    CAROUSEL_BANNER_TOP_LOCATOR = (By.XPATH, "//*[@id='carousel-banner-0']")
    CAROUSEL_BANNER_DOWN_LOCATOR = (By.XPATH, "//*[@id='carousel-banner-1']")
    CART_BUTTON_LOCATOR = (By.XPATH, "//div[@id='header-cart']")

    locators_list = [
        OPENCART_LOGO_LOCATOR,
        SEARCH_LOCATOR,
        CAROUSEL_BANNER_TOP_LOCATOR,
        CAROUSEL_BANNER_DOWN_LOCATOR,
        CART_BUTTON_LOCATOR
    ]

    def open_home_page(self, browser):
        browser.get(browser.base_url)

    def check_element_visible(self, browser, locator):
        WebDriverWait(browser, 10, poll_frequency=1).until(EC.visibility_of_element_located(locator))

    @pytest.mark.parametrize("locator", locators_list)
    def test_opencart_home_page_elements_visible(self, browser, locator):
        self.open_home_page(browser)
        self.check_element_visible(browser, locator)