
from pages.base_page import BasePage
from data.constants import Urls
from locators.locators import CatalogPageLocators


class CatalogPage(BasePage):

    def open_catalog(self):
        self.open(Urls.URL_CATALOG)

    def check_catalog_elements_visible(self, locator):
        self.check_element_visible(locator)

    def check_catalog_currency(self, currency):
        ref_price_eur = 189.86
        ref_price_gbp = 148.22
        ref_price_usd = 241.99

        price_product = self.get_find_element(CatalogPageLocators.PRICE_PRODUCT_LOCATOR)
        self.move_to_element(CatalogPageLocators.PRICE_PRODUCT_LOCATOR)

        if currency == "EUR":
            assert price_product.text[-1:] == '€', "Валюта отличается от выбранной"
            assert float(price_product.text[:-1]) == ref_price_eur, "Цена не соответствует выбранной валюте"
        elif currency == "GBP":
            assert price_product.text[:1] == '£', "Валюта отличается от выбранной"
            assert float(price_product.text[1:]) == ref_price_gbp, "Цена не соответствует выбранной валюте"
        elif currency == "USD":
            assert price_product.text[:1] == '$', "Валюта отличается от выбранной"
            assert float(price_product.text[1:]) == ref_price_usd, "Цена не соответствует выбранной валюте"
