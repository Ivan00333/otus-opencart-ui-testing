

class Db():
    def __init__(self, connection, logger):
        self.connection = connection
        self.logger = logger
        self.customer_table = 'bitnami_opencart.oc_customer'

    def create_user_in_db(self, user_data):
        self.logger.info(f"Создание пользователя в таблице {self.customer_table}")
        columns = ", ".join(user_data.keys())
        values = ", ".join(['%s'] * len(user_data))

        sql = (f"INSERT INTO {self.customer_table} "
               f"({columns} )"
               f"VALUES ({values});"
               )

        with self.connection.cursor() as cursor:
            cursor.execute(sql, tuple(user_data.values()))
            self.connection.commit()
            new_id = cursor.lastrowid

        self.logger.info(f"Создан пользователь с id = {new_id}")

        return new_id

    def get_user_from_db_by_id(self, user_id: int):
        self.logger.info(f"Получение строки из таблицы {self.customer_table} по id - {user_id}")
        sql = (
            "SELECT * "
            f"FROM {self.customer_table} "
            "WHERE customer_id = %s"
        )

        with self.connection.cursor() as cursor:
            cursor.execute(sql, (user_id))
            row = cursor.fetchone()

        return row

    def check_created_user_in_db(self, user_data_db: str, user_data: str):
        exclude = {"customer_id", "date_added"}
        user_data_from_db = {k: v for k, v in user_data_db.items() if k not in exclude}

        for key, val in user_data_from_db.items():
            value = user_data.get(key)
            assert key is not None, f"Ключ {key!r} отсутствует в в данных пользователя>"
            assert value == val, f"{key!r}: ожидали {val!r}, получили {value!r}"

        customer_id = user_data_db["customer_id"]
        assert customer_id > 0, f"Customer_id равен = {customer_id}"

    def check_updated_user(self, update_data: dict, data_from_db: dict):
        for key, val in update_data.items():
            value = data_from_db.get(key)
            assert value == val, f"{key!r}: ожидали {val!r}, получили {value!r}"

    def delete_user_by_id(self, user_id: int):
        self.logger.info(f"Удаление пользователя из таблицы {self.customer_table} с id - {user_id}")
        sql = (
            f"DELETE FROM {self.customer_table} "
            "WHERE customer_id = %s"
        )

        with self.connection.cursor() as cursor:
            cursor.execute(sql, (user_id))
            self.connection.commit()
            self.logger.info(f"Пользователь с id={user_id} удален")
            return cursor.rowcount

    def update_user(self, user_id: int, parameters_to_change: dict, ):
        self.logger.info(f"Изменение пользователя с id = {user_id}")
        if not parameters_to_change:
            raise ValueError("Пустой словарь updates")

        set_vol = ", ".join(f"{key} = %s" for key in parameters_to_change.keys())

        sql = (
            f"UPDATE {self.customer_table} "
            f"SET {set_vol} "
            "WHERE customer_id = %s"
        )

        params = list(parameters_to_change.values()) + [user_id]

        with self.connection.cursor() as cursor:
            cursor.execute(sql, params)
            self.connection.commit()

        return cursor.rowcount

    def get_rows_from_db(self, rows_count: int):
        sql = f"SELECT * FROM {self.customer_table} LIMIT %s"

        with self.connection.cursor() as cursor:
            cursor.execute(sql, (rows_count))
            rows = cursor.fetchall()

            return rows
