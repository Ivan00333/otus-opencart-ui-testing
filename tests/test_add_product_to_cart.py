import allure

from pages.add_product_to_cart import AddToCart


class TestAddToCart:
    @allure.title("Проверка добавления товара в корзину")
    def test_add_to_cart(self, driver, logger):
        page = AddToCart(driver, logger)
        page.open_home_page()
        page.add_product_to_cart()
        page.check_elements_in_cart()
        page.check_price_in_cart()
