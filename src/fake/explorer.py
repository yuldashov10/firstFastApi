from faker import Faker

from src.model.explorer import Explorer

__all__ = ["FakeExplorerData"]

fake = Faker()


class FakeExplorerData:
    def __init__(self, count: int = 20):
        self.__count = count
        self.__explorers: list[Explorer] = [
            Explorer(**self._get_fake_explorer())
            for _ in range(self.__count)
        ]

    def _get_fake_explorer(self) -> dict[str, str]:
        return {
            "name": fake.name(),
            "country": fake.country_code(),
            "description": fake.text(50),
        }

    def list(self) -> list[Explorer]:
        """Список исследователей."""
        return self.__explorers

    def get(self, name: str) -> Explorer | None:
        """
        Получение исследователя по имени.

        :param name: Имя исследователя.
        :return: None, если исследователь не найден.
        """
        for explorer in self.__explorers:
            if explorer.name.lower() == name.lower():
                return explorer
        return

    def create(self, explorer: Explorer) -> Explorer:
        """Создание нового исследователя."""
        # new_explorer: Explorer = Explorer(**self._get_fake_explorer())
        # self.__explorers.append(new_explorer)
        # return new_explorer

        return explorer

    def modify(self, explorer: Explorer) -> Explorer:
        """Частичное изменение записи исследователя."""
        return explorer

    def replace(self, explorer: Explorer) -> Explorer:
        """Полная замена записи исследователя."""
        return explorer

    def delete(self, name: str) -> None:
        """
        Удаление записи исследователя.
        :return: None, если запись существовала.
        """
        return


if __name__ == "__main__":
    fake_explorer = FakeExplorerData()

    for explorer in fake_explorer.list():
        print(f"{explorer.name} | {explorer.country}")
