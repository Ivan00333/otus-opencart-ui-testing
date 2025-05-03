import re

import pytest
from conftest import connection
from logger.logger import Logger
from pages.register_page import RegisterPage
import bcrypt
from datetime import datetime


class Db(Logger):
    def __init__(self, connection, test_name):
        self.connection = connection
        self.user = RegisterPage.create_user()
        self.logger = self._config_logger(test_name)

    def create_user_data(self):
        self.logger.info("Создание данных пользователя для БД")
        new_user = self.user

        salt = bcrypt.gensalt(rounds=10)
        hashed = bcrypt.hashpw(new_user["password"].encode(), salt)
        hashed_password =hashed.decode()

        now = datetime.now()
        formatted = now.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]

        user_data = {
            "customer_group_id": 0,
            "store_id": 0,
            "language_id": 1,
            "firstname": new_user["firstname"],
            "lastname": new_user["lastname"],
            "email": new_user["email"],
            "telephone": new_user["telephone"],
            "password": hashed_password,
            "custom_field": "",
            "newsletter": 0,
            "ip": '192.168.0.10',
            "status": 1,
            "safe": 0,
            "token": "",
            "code": "",
            "date_added": formatted
        }

        return user_data

    def create_user(self, user_data):
        self.logger.info("Создание пользователя в таблице bitnami_opencart.oc_customer")
        columns = ", ".join(user_data.keys())
        values = ", ".join(['%s'] * len(user_data))

        sql = ("INSERT INTO bitnami_opencart.oc_customer "
               f"({columns} )"
               f"VALUES ({values});"
               )

        with self.connection.cursor() as cursor:
            cursor.execute(sql, tuple(user_data.values()))
            self.connection.commit()
            new_id = cursor.lastrowid

        return new_id

    def get_user_from_db_by_id(self, user_id: int):
        self.logger.info(f"Получение строки из таблицы bitnami_opencart.oc_customer по id - {user_id}")
        sql = (
            "SELECT * "
            "FROM bitnami_opencart.oc_customer "
            "WHERE customer_id = %s"
        )

        with self.connection.cursor() as cursor:
            cursor.execute(sql, (user_id))
            row = cursor.fetchone()

        return row

    def check_created_userIn_db(self, user_data_db: str, user_data: str):
        exclude = {"customer_id", "date_added"}
        user_data_from_db = {k:v for k, v in user_data_db.items() if k not in exclude}

        for key, val in user_data_from_db.items():
            value = user_data.get(key)
            assert key is not None, f"Ключ {key!r} отсутствует в в данных пользователя>"
            assert value == val, f"{key!r}: ожидали {val!r}, получили {value!r}"

        dt = user_data_db["date_added"]
        date_from_db= dt.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]

        pattern = re.compile(r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{3}$")
        assert pattern.match(date_from_db), (
            f"Поле date_added = {date_from_db!r} не соответствует формату "
            "`YYYY-MM-DD HH:MM:SS.SSS`"
        )

        customer_id = user_data_db["customer_id"]
        assert isinstance(customer_id, int), f"Ожидали целочисленный ID, получили {type(customer_id)}"
        assert customer_id > 0, f"Customer_id равен = {customer_id}"


    def delete_user_by_id(self, user_id: int):
        self.logger.info(f"Удаление пользователя из таблицы bitnami_opencart.oc_customer с id - {user_id}")
        sql = (
            "DELETE FROM bitnami_opencart.oc_customer "
            "WHERE customer_id = %s"
        )

        with self.connection.cursor() as cursor:
            cursor.execute(sql, (user_id))
            self.connection.commit()
            self.logger.info(f"Пользователь с id={user_id} удален")


