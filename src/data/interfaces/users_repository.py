from abc import ABC ,abstractmethod
from typing import List

from src.domain.models.users import Users

class UsersRepositoryInterface(ABC):

  @abstractmethod
  def insert_user(self, first_name: str, last_name: str, age: int) -> None:
    raise NotImplementedError("'insert_user' must be implemented")

  @abstractmethod
  def select_user(self, first_name: str) -> List[Users]:
    raise NotImplementedError("'select_user' must be implemented")

  @abstractmethod
  def list_users(self) -> List[Users]:
    raise NotImplementedError("'list_user' must be implemented")

  @abstractmethod
  def delete_user(self, id:int) -> Users:
    raise NotImplementedError("'delete_user' must be implemented")

  @abstractmethod
  def update_user(self, id:int,first_name: str, last_name: str, age: int) -> Users:
    raise NotImplementedError("'update_user' must be implemented")
