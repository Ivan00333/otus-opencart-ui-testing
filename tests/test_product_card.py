import allure
import pytest
from pages.product_card_page import ProductCardPage
from locators.locators import ProductCardCatalogLocators


class TestProductCard:
    @allure.title("Проверка элементов на странице товара")
    @pytest.mark.parametrize("locator", ProductCardCatalogLocators.locators_list)
    def test_check_visible_product_card_elements(self, driver, locator, logger):
        page = ProductCardPage(driver, logger)
        page.open_product_card_page()
        page.check_element_visible(locator)
