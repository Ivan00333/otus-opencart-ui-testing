from faker import Faker
from pages.base_page import BasePage
from data.constants import Urls
from locators.locators import RegisterPageLocators as rpl


class RegisterPage(BasePage):
    def open_register_page(self):
        self.open(Urls.URL_REGISTER_PAGE)

    def fill_registration_user_form(self):
        fake = Faker()
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.email()
        password = fake.password()

        self.input(rpl.FIRST_NAME_LOCATOR, first_name)
        self.input(rpl.LAST_NAME_LOCATOR, last_name)
        self.input(rpl.EMAIL_LOCATOR, email)
        self.input(rpl.PASSWORD_LOCATOR, password)
        self.click(rpl.AGREE_POLICY_LOCATOR)
        self.click(rpl.CONTINUE_BUTTON_LOCATOR)


    def check_success_registration(self):
        self.check_element_visible(rpl.SUCCESS_REGISTRATION_MESSAGE)