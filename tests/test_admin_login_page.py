import allure
import pytest
from pages.admin_login_page import AdminLoginPage
from locators.locators import AdminLoginPageLocators


class TestAdminLoginPage:
    @allure.title("Проверка страницы авторизации администратора")
    @pytest.mark.parametrize("locator", AdminLoginPageLocators.locators_list)
    def test_check_visible_admin_login_elements(self, driver, locator, logger):
        page = AdminLoginPage(driver, logger)
        page.open_admin_login_page()
        page.check_element_visible(locator)
