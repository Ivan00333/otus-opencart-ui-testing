
from selenium.webdriver.common.by import By


class AdminLoginPageLocators:
    CARD_HEADER_LOCATOR = (By.XPATH, "//div[text()=' Please enter your login details.']")
    INPUT_USERNAME_LOCATOR = (By.XPATH, "//input[@id='input-username']")
    INPUT_PASSWORD_LOCATOR = (By.XPATH, "//input[@id='input-password']")
    LOGO_OPENCART_LOCATOR = (By.XPATH, "//a/img[@title='OpenCart']")
    BUTTON_LOGIN_LOCATOR = (By.XPATH, "//button[text()=' Login']")

    locators_list = [
        CARD_HEADER_LOCATOR,
        INPUT_USERNAME_LOCATOR,
        INPUT_PASSWORD_LOCATOR,
        LOGO_OPENCART_LOCATOR,
        BUTTON_LOGIN_LOCATOR
    ]


class AdminPageLocators:
    ADMIN_USERNAME = 'user'
    ADMIN_PASSWORD = 'bitnami'

    INPUT_USERNAME_LOCATOR = (By.XPATH, "//input[@id='input-username']")
    INPUT_PASSWORD_LOCATOR = (By.XPATH, "//input[@id='input-password']")
    BUTTON_LOGIN_LOCATOR = (By.XPATH, "//div[@class='text-end']/button[@type='submit']")
    ADMIN_NAME_LOCATOR = (By.XPATH, "//span[contains(text(), 'John Doe')]")
    BUTTON_LOGOUT_LOCATOR = (By.XPATH, "//span[text()='Logout']")
    CATALOG_LOCATOR = (By.XPATH, "//a[text()=' Catalog']")
    PRODUCTS_LOCATOR = (By.XPATH, "//a[text()='Products']")
    ADD_PRODUCTS_BUTTON_LOCATOR = (By.CSS_SELECTOR, ".btn .fa-plus")
    FIELD_PRODUCT_NAME_LOCATOR = (By.XPATH, "//input[@placeholder='Product Name']")
    DATA_BUTTON_LOCATOR = (By.XPATH, "//a[text()='Data']")
    FIELD_MODEL_LOCATOR = (By.XPATH, "//input[@placeholder='Model']")
    FIELD_META_TAG_LOCATOR = (By.XPATH, "//input[@placeholder='Meta Tag Title']")
    SEO_BUTTON_LOCATOR = (By.XPATH, "//a[text()='SEO']")
    FIELD_KEYWORD_LOCATOR = (By.XPATH, "//input[@placeholder='Keyword']")
    SAVE_PRODUCT_BUTTON_LOCATOR = (By.CSS_SELECTOR, ".fa-floppy-disk")
    CHECKBOX_LOCATOR = (By.XPATH, "//tbody/tr[1]//input[@type='checkbox']")
    DELETE_PRODUCT_BUTTON_LOCATOR = (By.CSS_SELECTOR, ".btn-danger")


class AddToCartLocators:
    ADD_TO_CART_BUTTON_LOCATOR = (By.XPATH, "//div[@class='col mb-3'][2]//button[@type='submit'][1]")
    CART_BUTTON_LOCATOR = (By.XPATH, "//div[@id='header-cart']")
    PRODUCT_NAME_LOCATOR = (By.XPATH, "//td/a[text()='iPhone']")
    PRODUCT_QUANTITY_LOCATOR = (By.XPATH, "//td[text()='x 1']")
    PRICE_PRODUCT_LOCATOR = (By.XPATH, "//div[@class='col mb-3'][2]//span[@class='price-new']")
    PRICE_PRODUCT_IN_CART_LOCATOR = (By.XPATH, "//table[@class='table table-striped mb-2']//td[@class='text-end'][2]")


class CatalogPageLocators:
    SORTING_MENU_LOCATOR = (By.XPATH, "//*[@id='display-control']")
    CATALOG_LIST_LOCATOR = (By.XPATH, "//*[@class='list-group mb-3']")
    PRODUCTS_TITLE_LOCATOR = (By.XPATH, "//div/h2[text()='Tablets']")
    HOME_PAGE_ICON_LOCATOR = (By.XPATH, "//div[@id='logo']/a[contains(@href, 'en-gb?route=common/home')]")
    HP_BANNER_LOCATOR = (By.XPATH, "//*[@alt='HP Banner']")
    TABLETS_BUTTON_LOCATOR = (By.XPATH, "//a[text()='Tablets']")
    PRICE_PRODUCT_LOCATOR = (By.XPATH, "//div[@class='col mb-3'][1]//span[@class='price-new']")

    locators_list = [SORTING_MENU_LOCATOR,
                     CATALOG_LIST_LOCATOR,
                     PRODUCTS_TITLE_LOCATOR,
                     HOME_PAGE_ICON_LOCATOR,
                     HP_BANNER_LOCATOR
                     ]


class HomePageLocators:
    OPENCART_LOGO_LOCATOR = (By.XPATH, "//img[contains(@src, 'opencart-logo.png')]")
    SEARCH_LOCATOR = (By.XPATH, "//input[@name='search']")
    CAROUSEL_BANNER_TOP_LOCATOR = (By.XPATH, "//*[@id='carousel-banner-0']")
    CAROUSEL_BANNER_DOWN_LOCATOR = (By.XPATH, "//*[@id='carousel-banner-1']")
    CART_BUTTON_LOCATOR = (By.XPATH, "//div[@id='header-cart']")

    locators_list = [
        OPENCART_LOGO_LOCATOR,
        SEARCH_LOCATOR,
        CAROUSEL_BANNER_TOP_LOCATOR,
        CAROUSEL_BANNER_DOWN_LOCATOR,
        CART_BUTTON_LOCATOR
    ]

    CURRENCY_BUTTON_LOCATOR = (By.XPATH, "//span[text()='Currency']")
    EUR_LOCATOR = (By.XPATH, "//li/a[@href='EUR']")
    GBP_LOCATOR = (By.XPATH, "//li/a[@href='GBP']")
    USD_LOCATOR = (By.XPATH, "//li/a[@href='USD']")
    PRICE_PRODUCT_LOCATOR = (By.XPATH, "//div[@class='col mb-3'][2]//span[@class='price-new']")


class ProductCardCatalogLocators:
    PRODUCT_IMAGE_LOCATOR = (By.XPATH, "//*[@class='image magnific-popup']")
    ADD_TO_CART_BUTTON_LOCATOR = (By.XPATH, "//*[text()='Add to Cart']")
    PRODUCT_NAME_LOCATOR = (By.XPATH, "//div/h1[text()='Samsung Galaxy Tab 10.1']")
    PRODUCT_PRICE_LOCATOR = (By.XPATH, "//*[@class='price-new']")
    PRODUCT_DESCRIPTION_LOCATOR = (By.XPATH, "//*[@class='tab-content']")

    locators_list = [
        PRODUCT_NAME_LOCATOR,
        ADD_TO_CART_BUTTON_LOCATOR,
        PRODUCT_NAME_LOCATOR,
        PRODUCT_PRICE_LOCATOR,
        PRODUCT_DESCRIPTION_LOCATOR
    ]


class RegisterPageLocators:
    FIRST_NAME_LOCATOR = (By.XPATH, "//input[@id='input-firstname']")
    LAST_NAME_LOCATOR = (By.XPATH, "//input[@id='input-lastname']")
    EMAIL_LOCATOR = (By.XPATH, "//input[@id='input-email']")
    PASSWORD_LOCATOR = (By.XPATH, "//input[@id='input-password']")
    CONTINUE_BUTTON_LOCATOR = (By.XPATH, "//button[text()='Continue']")
    SUCCESS_REGISTRATION_MESSAGE = (By.XPATH, "//h1[text()='Your Account Has Been Created!']")
    AGREE_POLICY_LOCATOR = (By.XPATH, "//input[@name='agree']")

    locators_list = [
        FIRST_NAME_LOCATOR,
        LAST_NAME_LOCATOR,
        EMAIL_LOCATOR,
        PASSWORD_LOCATOR,
        CONTINUE_BUTTON_LOCATOR
    ]
