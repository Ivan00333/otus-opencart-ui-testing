import allure
from pages.base_page import BasePage
from data.constants import Urls


class ProductCardPage(BasePage):
    @allure.step("Открытие карточки продукта")
    def open_product_card_page(self):
        self.open(f"{self.driver.base_url}{Urls.URL_PRODUCT_CARD}")
