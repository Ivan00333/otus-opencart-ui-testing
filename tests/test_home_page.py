from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestHomePage:
    OPENCART_LOGO_LOCATOR = "//img[contains(@src, 'opencart-logo.png')]"
    SEARCH_LOCATOR = "//input[@name='search']"
    CAROUSEL_BANNER_TOP_LOCATOR = "//*[@id='carousel-banner-0']"
    CAROUSEL_BANNER_DOWN_LOCATOR = "//*[@id='carousel-banner-1']"
    CART_BUTTON_LOCATOR = "//div[@id='header-cart']"

    def open_home_page(self, browser):
        browser.get(browser.base_url)

    def check_element_visible(self, browser, locator):
        WebDriverWait(browser, 10, poll_frequency=1).until(EC.visibility_of_element_located((By.XPATH, locator)))

    def test_opencart_logo_visible(self, browser):
        self.open_home_page(browser)
        self.check_element_visible(browser, self.OPENCART_LOGO_LOCATOR)

    def test_search_visible(self, browser):
        self.open_home_page(browser)
        self.check_element_visible(browser, self.SEARCH_LOCATOR)

    def test_top_carousel_visible(self, browser):
        self.open_home_page(browser)
        self.check_element_visible(browser, self.CAROUSEL_BANNER_TOP_LOCATOR)

    def test_down_carousel_visible(self, browser):
        self.open_home_page(browser)
        self.check_element_visible(browser, self.CAROUSEL_BANNER_DOWN_LOCATOR)

    def test_cart_button_visible(self, browser):
        self.open_home_page(browser)
        self.check_element_visible(browser, self.CART_BUTTON_LOCATOR)



