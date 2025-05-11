import allure
import pytest
from pages.home_page import HomePage
from locators.locators import HomePageLocators


class TestHomePage:
    @allure.title("Проверка элементов на домашней странице")
    @pytest.mark.parametrize("locator", HomePageLocators.locators_list)
    def test_opencart_home_page_elements_visible(self, driver, locator, logger):
        page = HomePage(driver, logger)
        page.open_home_page()
        page.check_element_visible(locator)
