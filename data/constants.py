
import enum


class Urls(enum.auto):
    BASE_URL = 'http://192.168.0.10:8081'

    URL_ADMIN_LOGIN_PAGE = "/administration"
    URL_CATALOG = "/en-gb/catalog/tablet"
    URL_PRODUCT_CARD = "/en-gb/product/tablet/samsung-galaxy-tab-10-1"
    URL_REGISTER_PAGE = "/en-gb?route=account/register"


class AdminAuth(enum.auto):
    ADMIN_USERNAME = 'user'
    ADMIN_PASSWORD = 'bitnami'


class Currency(enum.auto):
    LIST_CURRENCY = ['EUR', 'GBP', 'USD']
