
import pytest
from pages.register_page import RegisterPage
from locators.locators import RegisterPageLocators


class TestRegisterPage:
    @pytest.mark.parametrize("locator", RegisterPageLocators.locators_list)
    def test_check_visible_register_page_elements(self, driver, locator):
        page = RegisterPage(driver)
        page.open_register_page()
        page.check_element_visible(locator)
