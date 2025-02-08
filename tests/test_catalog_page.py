import allure
import pytest
from pages.catalog_page import CatalogPage
from locators.locators import CatalogPageLocators


class TestCatalogPage:

    @allure.title("Проверка элементов на странице каталога")
    @pytest.mark.parametrize("locator", CatalogPageLocators.locators_list)
    def test_check_visible_catalog_elements(self, driver, locator):
        page = CatalogPage(driver)
        page.open_catalog()
        page.check_catalog_elements_visible(locator)
