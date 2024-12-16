
import pytest
from pages.home_page import HomePage
from locators.locators import HomePageLocators
from data.constants import Currency


class TestCurrency:
    @pytest.mark.parametrize('currency', Currency.LIST_CURRENCY)
    def test_currency(self, driver, currency):
        page = HomePage(driver)
        page.open_home_page()
        page.choice_currency(currency)
        page.check_curency(currency)