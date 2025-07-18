from typing import List

from src.infra.db.settings.connection import DBconnectionHandler
from src.infra.db.entities.users import Users as UsersEntity
from src.data.interfaces.users_repository import UsersRepositoryInterface
from src.domain.models.users import Users

class UsersRepository(UsersRepositoryInterface):

    @classmethod
    def insert_user(cls, first_name: str, last_name: str, age: int) -> None:
        with DBconnectionHandler() as database:
            try:
                new_registry = UsersEntity(
                first_name=first_name,
                last_name=last_name,
                age=age
                )

                database.session.add(new_registry)
                database.session.commit()

            except Exception as exception:
                database.session.rollback()
                raise exception

    @classmethod
    def select_user(cls, first_name: str) -> List[Users]:
        with DBconnectionHandler() as database:
            try:
                users = (
                    database.session
                    .query(UsersEntity)
                    .filter(UsersEntity.first_name == first_name)
                    .all()
                )
                return users
            except Exception as exception:
                database.session.rollback()
                raise exception

    @classmethod
    def list_users(cls) -> List[Users]:
        with DBconnectionHandler() as database:
            try:
                users = (
                    database.session
                    .query(UsersEntity)
                    .all()
                )
                return users
            except Exception as exception:
                database.session.rollback()
                raise exception

    @classmethod
    def delete_user(cls, id:int) -> Users:
        with DBconnectionHandler() as database:
            try:
                user = database.session.query(UsersEntity).filter(UsersEntity.id == id).first()

                if user:
                    database.session.delete(user)
                    database.session.commit()

                return user

            except Exception as exception:
                database.session.rollback()
                raise exception

    @classmethod
    def update_user(cls, id: int, first_name: str, last_name: str, age: int) -> Users:
        with DBconnectionHandler() as database:
            try:
                user = database.session.query(UsersEntity).filter(UsersEntity.id == id).first()

                if user:
                    user.first_name = first_name
                    user.last_name = last_name
                    user.age = age

                    database.session.commit()

                    database.session.refresh(user)
                    database.session.expunge(user)

                return user

            except Exception as exception:
                database.session.rollback()
                raise exception
