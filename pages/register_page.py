import allure
from faker import Faker
from pages.base_page import BasePage
from data.constants import Urls
from locators.locators import RegisterPageLocators as rpl


class RegisterPage(BasePage):
    @allure.step("Открытие страницы регистрации")
    def open_register_page(self):
        self.open(f"{self.driver.base_url}{Urls.URL_REGISTER_PAGE}")

    @staticmethod
    @allure.step("Создание пользователя")
    def create_user():
        fake = Faker()
        user_data = {
            "firstname": fake.first_name(),
            "lastname": fake.last_name(),
            "email": fake.email(),
            "password": fake.password(6),
            "telephone": fake.phone_number()
        }

        return user_data

    @allure.step("Заполнение полей регистрации пользователя")
    def fill_registration_user_form(self):
        user_data = RegisterPage.create_user()

        self.input(rpl.FIRST_NAME_LOCATOR, user_data["firstname"])
        self.input(rpl.LAST_NAME_LOCATOR, user_data["lastname"])
        self.input(rpl.EMAIL_LOCATOR, user_data["email"])
        self.input(rpl.PASSWORD_LOCATOR, user_data["password"])
        self.click(rpl.AGREE_POLICY_LOCATOR)
        self.click(rpl.CONTINUE_BUTTON_LOCATOR)

    @allure.step("Проверка, что регистрация прошла успешно")
    def check_success_registration(self):
        self.check_element_visible(rpl.SUCCESS_REGISTRATION_MESSAGE)

