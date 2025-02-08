import allure

from pages.admin_login_page import AdminLoginPage
from pages.admin_page import AdminPage


class TestAdminLogin:
    @allure.title("Проверка авторизации администратора")
    def test_admin_auth(self, driver):
        admin_login_page = AdminLoginPage(driver)
        admin_page = AdminPage(driver)
        admin_login_page.open_admin_login_page()
        admin_login_page.admin_auth()
        admin_page.check_admin_auth()
        admin_page.logout()
