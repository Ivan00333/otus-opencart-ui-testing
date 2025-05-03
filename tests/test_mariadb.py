import pytest
from db.db import Db



def test_create_user(connection):
    db = Db(connection, "test_create_user")
    user_data = db.create_user_data()
    id = db.create_user(user_data)
    user_form_db = db.get_user_from_db_by_id(user_id=id)
    print(user_data)
    db.check_created_userIn_db(user_form_db, user_data)
    db.delete_user_by_id(id)
