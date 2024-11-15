from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestAddToCart:
    ADD_TO_CART_BUTTON_LOCATOR = (By.XPATH, "//div[@class='col mb-3'][2]//button[@type='submit'][1]")
    CART_BUTTON_LOCATOR = (By.XPATH, "//div[@id='header-cart']")
    PRODUCT_NAME_LOCATOR = (By.XPATH, "//td/a[text()='iPhone']")
    PRODUCT_QUANTITY_LOCATOR = (By.XPATH, "//td[text()='x 1']")
    PRICE_PRODUCT_LOCATOR = (By.XPATH, "//div[@class='col mb-3'][2]//span[@class='price-new']")
    PRICE_PRODUCT_IN_CART_LOCATOR = (By.XPATH, "//table[@class='table table-striped mb-2']//td[@class='text-end'][2]")

    def open_home_page(self, browser):
        browser.get(browser.base_url)

    def get_find_element(self, browser, locator):
        return WebDriverWait(browser, 10, poll_frequency=1).until(EC.visibility_of_element_located(locator))

    def check_element_visible(self, browser, locator):
        WebDriverWait(browser, 10, poll_frequency=1).until(EC.visibility_of_element_located(locator))

    def test_add_to_cart(self, browser):
        self.open_home_page(browser)

        button_add_to_cart = self.get_find_element(browser, self.ADD_TO_CART_BUTTON_LOCATOR)
        actions = ActionChains(browser)
        actions.move_to_element(button_add_to_cart).perform()
        button_add_to_cart = WebDriverWait(browser, 10).until(EC.element_to_be_clickable(self.ADD_TO_CART_BUTTON_LOCATOR))
        button_add_to_cart.click()

        cart_button = self.get_find_element(browser, self.CART_BUTTON_LOCATOR)
        actions.move_to_element(cart_button).perform()
        cart_button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable(self.CART_BUTTON_LOCATOR))
        cart_button.click()

        self.check_element_visible(browser, self.PRODUCT_NAME_LOCATOR)
        self.check_element_visible(browser, self.PRODUCT_QUANTITY_LOCATOR)
        self.check_element_visible(browser, self.PRICE_PRODUCT_IN_CART_LOCATOR)

        price_product = self.get_find_element(browser, self.PRICE_PRODUCT_LOCATOR).text
        price_product_in_cart = self.get_find_element(browser, self.PRICE_PRODUCT_IN_CART_LOCATOR).text

        assert price_product[0] == price_product_in_cart[0], f"Валюта в корзине должна быть {price_product[0]}"
        assert float(price_product[1:]) == float(price_product_in_cart[1:]), "Цена продукта отличается от цены в корзине"
