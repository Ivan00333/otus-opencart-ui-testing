
import pytest
from pages.admin_login_page import AdminLoginPage
from locators.locators import AdminLoginPageLocators


class TestAdminLoginPage:

    @pytest.mark.parametrize("locator", AdminLoginPageLocators.locators_list)
    def test_check_visible_admin_login_elements(self, driver, locator):
        page = AdminLoginPage(driver)
        page.open_admin_login_page()
        page.check_element_visible(locator)
