from db.db import Db


class TestDb:

    def test_create_user(self, db, user_data):
        id = db.create_user_in_db(user_data)
        user_form_db = db.get_user_from_db_by_id(user_id=id)
        db.check_created_user_in_db(user_form_db, user_data)

    def test_update_user(self, db, user_data):

        data_for_update = {
            "firstname": "New",
            "lastname": "Name",
            "email": "new.email@example.com",
            "telephone": "1111"
        }

        user_id = db.create_user_in_db(user_data)
        db.update_user(user_id, data_for_update)
        updated_data = db.get_user_from_db_by_id(user_id)
        db.check_updated_user(update_data=data_for_update, data_from_db=updated_data)

    def test_negative_update_user(self, db):

        data_for_update = {
            "firstname": "New",
            "lastname": "Name"
        }

        user_id = 99999
        row_count = db.update_user(user_id, data_for_update)
        assert row_count == 0, f"Ожидали 0 обновлённых строк, но обновлено: {row_count}"

    def test_delete_user(self, db, user_data):
        rows = db.get_rows_from_db(1)

        if rows:
            user_data = rows[0]
            user_id = user_data["customer_id"]
            db.delete_user_by_id(user_id)
        else:
            user_id = db.create_user_in_db(user_data)
            db.delete_user_by_id(user_id)

        row = db.get_user_from_db_by_id(user_id)
        assert row is None, f"Запись c customer_id={user_id} есть в таблице"

    def test_delete_user_negative(self, db):
        row_count = db.delete_user_by_id(99999999)
        assert row_count == 0, "Ожидали, что будет удалено 0 строк"
