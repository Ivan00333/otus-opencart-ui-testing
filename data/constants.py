
import enum


class Urls(enum.auto):
    BASE_URL = 'http://192.168.0.10:8081'

    URL_ADMIN_LOGIN_PAGE = f"{BASE_URL}/administration"
    URL_CATALOG = f"{BASE_URL}/en-gb/catalog/tablet"

class AdminAuth(enum.auto):
    ADMIN_USERNAME = 'user'
    ADMIN_PASSWORD = 'bitnami'

class Currency(enum.auto):
    LIST_CURRENCY = ['EUR', 'GBP', 'USD']