
from data.constants import Urls
from pages.base_page import BasePage
from locators.locators import HomePageLocators as locators
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    def open_home_page(self):
        self.open(Urls.BASE_URL)

    def check_element(self, locator):
        self.check_element_visible(locator)

    def choice_currency(self, currency):
        self.click(locators.CURRENCY_BUTTON_LOCATOR)
        currency_locator = (By.XPATH, f"//li/a[@href='{currency}']")
        currency = self.get_find_element(currency_locator)
        currency.click()

    def check_curency(self, currency):
        price_product = self.get_find_element(locators.PRICE_PRODUCT_LOCATOR)
        self.move_to_element(locators.PRICE_PRODUCT_LOCATOR)
        ref_price_eur = 96.66
        ref_price_gbp = 75.46
        ref_price_usd = 123.20
        
        if currency == "EUR":
            assert price_product.text[-1:] == '€', "Валюта отличается от выбранной"
            assert float(price_product.text[:-1]) == ref_price_eur, "Цена не соответствует выбранной валюте"
        elif currency == "GBP":
            assert price_product.text[:1] == '£', "Валюта отличается от выбранной"
            assert float(price_product.text[1:]) == ref_price_gbp, "Цена не соответствует выбранной валюте"
        elif currency == "USD":
            assert price_product.text[:1] == '$', "Валюта отличается от выбранной"
            assert float(price_product.text[1:]) == ref_price_usd, "Цена не соответствует выбранной валюте"
