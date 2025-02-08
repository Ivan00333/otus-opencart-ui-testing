import allure
import pytest
from pages.home_page import HomePage
from locators.locators import HomePageLocators


class TestHomePage:
    @allure.title("Проверка элементов на домашней странице")
    @pytest.mark.parametrize("locator", HomePageLocators.locators_list)
    def test_opencart_home_page_elements_visible(self, driver, locator):
        page = HomePage(driver)
        page.open_home_page()
        page.check_element_visible(locator)
