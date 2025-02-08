import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators.locators import AdminPageLocators


class AdminPage(BasePage):
    @allure.step("Проверка, что администартор авторизован")
    def check_admin_auth(self):
        self.check_element_visible(AdminPageLocators.ADMIN_NAME_LOCATOR)

    @allure.step("Выход")
    def logout(self):
        self.click(AdminPageLocators.BUTTON_LOGOUT_LOCATOR)

    @allure.step("Добавление нового продукта")
    def add_new_product(self):
        self.click(AdminPageLocators.CATALOG_LOCATOR)
        self.click(AdminPageLocators.PRODUCTS_LOCATOR)
        self.click(AdminPageLocators.ADD_PRODUCTS_BUTTON_LOCATOR)
        self.input(AdminPageLocators.FIELD_PRODUCT_NAME_LOCATOR, "A-Test")
        self.input(AdminPageLocators.FIELD_META_TAG_LOCATOR, "A-Test 1")
        self.click(AdminPageLocators.DATA_BUTTON_LOCATOR)
        self.input(AdminPageLocators.FIELD_MODEL_LOCATOR, "A-Test Model")
        self.click(AdminPageLocators.SEO_BUTTON_LOCATOR)
        self.input(AdminPageLocators.FIELD_KEYWORD_LOCATOR, "A-Test")
        self.click(AdminPageLocators.SAVE_PRODUCT_BUTTON_LOCATOR)

    @allure.step("Прверка списка продуктов")
    def check_product_in_list(self, product_name: str):
        self.click(AdminPageLocators.PRODUCTS_LOCATOR)
        self.check_element_visible((By.XPATH, f"//td[contains(text(), {product_name})]"))

    @allure.step("Удаление продукта")
    def delete_product(self):
        self.click(AdminPageLocators.CATALOG_LOCATOR)
        self.click(AdminPageLocators.PRODUCTS_LOCATOR)
        checkbox = self.get_find_element(AdminPageLocators.CHECKBOX_LOCATOR)
        checkbox.click()
        checkbox_value = checkbox.get_attribute("value")
        self.click(AdminPageLocators.DELETE_PRODUCT_BUTTON_LOCATOR)
        self.switch_to_alert_and_accept()
        self.check_element_not_visible((By.XPATH, f"//input[@value='{checkbox_value}']"))
