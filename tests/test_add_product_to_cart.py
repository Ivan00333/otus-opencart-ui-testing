
from pages.add_product_to_cart import AddToCart


class TestAddToCart:
    def test_add_to_cart(self, driver):
        page = AddToCart(driver)
        page.open_home_page()
        page.add_product_to_cart()
        page.check_elements_in_cart()
        page.check_price_in_cart()
