from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestCatalogPage:
    URI_CATALOG = '/en-gb/catalog/tablet'
    SORTING_MENU_LOCATOR = (By.XPATH, "//*[@id='display-control']")
    CATALOG_LIST_LOCATOR = (By.XPATH, "//*[@class='list-group mb-3']")
    PRODUCTS_TITLE_LOCATOR = (By.XPATH, "//div/h2[text()='Tablets']")
    HOME_PAGE_ICON_LOCATOR = (By.XPATH, "//div[@id='logo']/a[contains(@href, 'en-gb?route=common/home')]")
    HP_BANNER_LOCATOR = (By.XPATH, "//*[@alt='HP Banner']")

    def open_catalog_page(self, browser):
        browser.get(f"{browser.base_url}{self.URI_CATALOG}")

    def check_element_visible(self, browser, locator):
        WebDriverWait(browser, 10, poll_frequency=1).until(EC.visibility_of_element_located(locator))

    def test_catalog_list_visible(self, browser):
        self.open_catalog_page(browser)
        self.check_element_visible(browser, self.CATALOG_LIST_LOCATOR)

    def test_sorting_menu_visible(self, browser):
        self.open_catalog_page(browser)
        self.check_element_visible(browser, self.SORTING_MENU_LOCATOR)

    def test_product_title_visible(self, browser):
        self.open_catalog_page(browser)
        self.check_element_visible(browser, self.PRODUCTS_TITLE_LOCATOR)

    def test_home_page_icon_visible(self, browser):
        self.open_catalog_page(browser)
        self.check_element_visible(browser, self.HOME_PAGE_ICON_LOCATOR)

    def test_hp_banner_visible(self, browser):
        self.open_catalog_page(browser)
        self.check_element_visible(browser, self.HP_BANNER_LOCATOR)