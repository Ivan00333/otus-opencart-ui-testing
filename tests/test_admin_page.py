import allure

from pages.admin_page import AdminPage
from pages.admin_login_page import AdminLoginPage


class TestProduct:
    @allure.title("Создание нового продукта на странице администратора")
    def test_add_product(self, driver):
        page = AdminPage(driver)
        admin_login_page = AdminLoginPage(driver)
        admin_login_page.open_admin_login_page()
        admin_login_page.admin_auth()
        page.add_new_product()
        page.check_product_in_list('A-Test')

    @allure.title("Удаление продукта на странице администратора")
    def test_delete_product(self, driver):
        page = AdminPage(driver)
        admin_login_page = AdminLoginPage(driver)
        admin_login_page.open_admin_login_page()
        admin_login_page.admin_auth()
        page.delete_product()
