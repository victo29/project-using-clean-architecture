from sqlalchemy import text
import pytest

from src.infra.db.settings.connection import DBconnectionHandler
from src.infra.db.repositories.users_repository import UsersRepository

db_connection_handler = DBconnectionHandler()
connection = db_connection_handler.get_engine().connect()

@pytest.mark.skip(reason="Sentitive test")
def test_insert_user():

    mocked_first_name = "first"
    mocked_last_name = 'last'
    mocked_age = 18

    user_repository = UsersRepository()
    user_repository.insert_user(mocked_first_name, mocked_last_name, mocked_age)

    sql = """SELECT * FROM users WHERE first_name = '{}' AND last_name = '{}' AND age = '{}'
    """.format(mocked_first_name, mocked_last_name, mocked_age)

    response = connection.execute(text(sql))
    registry = response.fetchall()[0]

    assert registry.first_name == mocked_first_name
    assert registry.last_name == mocked_last_name
    assert registry.age == mocked_age


    print()
    print(registry)

    connection.execute(text(f"""
        DELETE FROM users WHERE id = {registry.id}
    """))
    connection.commit()

@pytest.mark.skip(reason="Sentitive test")
def test_select_user():
    mocked_first_name = "first_2"
    mocked_last_name = 'last_2'
    mocked_age = 19

    sql = """
    INSERT INTO users (first_name, last_name, age) VALUES ('{}', '{}', '{}')
    """.format(mocked_first_name, mocked_last_name, mocked_age)

    connection.execute(text(sql))
    connection.commit()

    user_repository = UsersRepository()
    response = user_repository.select_user(mocked_first_name)

    assert response[0].first_name == mocked_first_name
    assert response[0].last_name == mocked_last_name
    assert response[0].age == mocked_age

    connection.execute(text(f"""
        DELETE FROM users WHERE id = {response[0].id}
    """))

    connection.commit()
