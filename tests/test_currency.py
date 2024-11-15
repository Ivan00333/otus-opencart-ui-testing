import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestCurrency:
    CURRENCY_BUTTON_LOCATOR = (By.XPATH, "//span[text()='Currency']")
    EUR_LOCATOR = (By.XPATH, "//li/a[@href='EUR']")
    GBP_LOCATOR = (By.XPATH, "//li/a[@href='GBP']")
    USD_LOCATOR = (By.XPATH, "//li/a[@href='USD']")
    PRICE_PRODUCT_LOCATOR = (By.XPATH, "//div[@class='col mb-3'][2]//span[@class='price-new']")

    list_currency = [EUR_LOCATOR, GBP_LOCATOR, USD_LOCATOR]

    def open_home_page(self, browser):
        browser.get(browser.base_url)

    def get_find_element(self, browser, locator):
        return WebDriverWait(browser, 10, poll_frequency=1).until(EC.visibility_of_element_located(locator))

    def check_element_visible(self, browser, locator):
        WebDriverWait(browser, 10, poll_frequency=1).until(EC.visibility_of_element_located(locator))

    @pytest.mark.parametrize('currency', list_currency)
    def test_currency(self, browser, currency):
        self.open_home_page(browser)
        currency_button = self.get_find_element(browser, self.CURRENCY_BUTTON_LOCATOR)
        currency_button.click()
        currency = self.get_find_element(browser, currency)
        currency_current = currency.get_attribute("href")
        currency_current = currency_current.split("/")[-1]
        currency.click()

        price_product = self.get_find_element(browser, self.PRICE_PRODUCT_LOCATOR)
        actions = ActionChains(browser)
        actions.move_to_element(price_product).perform()
        ref_price_eur = 96.66
        ref_price_gbp = 75.46
        ref_price_usd = 123.20

        if currency_current == "EUR":
            assert price_product.text[-1:] == '€', "Валюта отличается от выбранной"
            assert float(price_product.text[:-1]) == ref_price_eur, "Цена не соответствует выбранной валюте"
        elif currency_current == "GBP":
            assert price_product.text[:1] == '£', "Валюта отличается от выбранной"
            assert float(price_product.text[1:]) == ref_price_gbp, "Цена не соответствует выбранной валюте"
        elif currency_current == "USD":
            assert price_product.text[:1] == '$', "Валюта отличается от выбранной"
            assert float(price_product.text[1:]) == ref_price_usd, "Цена не соответствует выбранной валюте"
