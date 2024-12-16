
from pages.base_page import BasePage
from data.constants import Urls


class RegisterPage(BasePage):
    def open_register_page(self):
        self.open(Urls.URL_REGISTER_PAGE)
