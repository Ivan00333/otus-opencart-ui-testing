
from pages.base_page import BasePage
from locators.locators import AddToCartLocators
from data.constants import Urls


class AddToCart(BasePage):
    locators = AddToCartLocators()

    list_locators = [
        locators.PRODUCT_NAME_LOCATOR,
        locators.PRODUCT_QUANTITY_LOCATOR,
        locators.PRICE_PRODUCT_IN_CART_LOCATOR
    ]

    def open_home_page(self):
        self.open(Urls.BASE_URL)

    def add_product_to_cart(self):
        self.move_to_element_and_click(self.locators.ADD_TO_CART_BUTTON_LOCATOR, timeout=10)
        self.move_to_element_and_click(self.locators.CART_BUTTON_LOCATOR)

    def check_elements_in_cart(self):
        self.check_elements_visible(self.list_locators)

    def check_price_in_cart(self):
        price_product = self.get_find_element(self.locators.PRICE_PRODUCT_LOCATOR).text
        price_product_in_cart = self.get_find_element(self.locators.PRICE_PRODUCT_IN_CART_LOCATOR).text

        assert price_product[0] == price_product_in_cart[0], f"Валюта в корзине должна быть {price_product[0]}"
        assert float(price_product[1:]) == float(price_product_in_cart[1:]), "Цена продукта отличается от цены в корзине"

