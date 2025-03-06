import allure
import pytest
from pages.home_page import HomePage
from data.constants import Currency


class TestCurrency:
    @allure.title("Проверка переключения валюты на главной странице")
    @pytest.mark.parametrize('currency', Currency.LIST_CURRENCY)
    def test_currency(self, driver, currency):
        page = HomePage(driver)
        page.open_home_page()
        page.choice_currency(currency)
        page.check_curency(currency)
