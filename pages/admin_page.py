
from pages.base_page import BasePage
from locators.locators import AdminPageLocators


class AdminPage(BasePage):
    def check_admin_auth(self):
        self.check_element_visible(AdminPageLocators.ADMIN_NAME_LOCATOR)

    def logout(self):
        self.click(AdminPageLocators.BUTTON_LOGOUT_LOCATOR)
