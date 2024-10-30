import pytest
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

    locators_list = [SORTING_MENU_LOCATOR,
                     CATALOG_LIST_LOCATOR,
                     PRODUCTS_TITLE_LOCATOR,
                     HOME_PAGE_ICON_LOCATOR,
                     HP_BANNER_LOCATOR
                     ]

    def open_catalog_page(self, browser):
        browser.get(f"{browser.base_url}{self.URI_CATALOG}")

    def check_element_visible(self, browser, locator):
        WebDriverWait(browser, 10, poll_frequency=1).until(EC.visibility_of_element_located(locator))

    @pytest.mark.parametrize("locator", locators_list)
    def test_check_visible_catalog_elements(self, browser, locator):
        self.open_catalog_page(browser)
        self.check_element_visible(browser, locator)
