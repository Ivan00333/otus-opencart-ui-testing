
import pytest
from pages.catalog_page import CatalogPage
from pages.home_page import HomePage
from data.constants import Currency


class TestCurrencyCatalog:
    @pytest.mark.parametrize('currency', Currency.LIST_CURRENCY)
    def test_catalog_currency(self, driver, currency):
        page = CatalogPage(driver)
        home_page = HomePage(driver)
        page.open_catalog()
        home_page.choice_currency(currency)
        page.check_catalog_currency(currency)
