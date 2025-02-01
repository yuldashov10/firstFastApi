from faker import Faker

from core.exceptions import ObjectDoesNotExist, DuplicateRecordError
from src.model.user import User

fake = Faker()


class FakeUserData:
    def __init__(self, count: int = 10):
        self.__count = count
        self.__users: list[User] = [
            User(**self._get_fake_user())
            for _ in range(self.__count)
        ]

    def find(self, username: str) -> User | None:
        for user in self.__users:
            if user.username == username:
                return user
        return None

    def user_exists(self, username: str) -> None:
        if not self.find(username):
            raise ObjectDoesNotExist(f"User '{username}' not found")

    def user_already_exists(self, username: str) -> None:
        if self.find(username):
            raise DuplicateRecordError(f"User '{username}' already exists")

    def _get_fake_user(self) -> dict[str, str]:
        return {
            "username": fake.user_name(),
            "password_hash": fake.password(length=12),
        }

    def list(self) -> list[User]:
        """Список пользователей."""
        return self.__users

    def get(self, username: str) -> User | None:
        """
        Получение пользователя по имя пользователя.

        :param username: Имя пользователя.
        :return: None, если пользователь не найден.
        """
        self.user_exists(username)
        return self.find(username)

    def create(self, user: User) -> User:
        """Создание нового пользователя."""
        self.user_already_exists(user.username)
        return user

    def modify(self, username: str, user: User) -> User:
        """Частичное изменение данных пользователя."""
        self.user_exists(username)
        return user

    def replace(self, user: User) -> User:
        """Полная замена записи существа."""
        return user

    def delete(self, username: str) -> None:
        """
        Удаление пользователя.
        :return: None, если запись существовала.
        """
        self.user_exists(username)
        return None
