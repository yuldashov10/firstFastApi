from faker import Faker

from src.model.creature import Creature

__all__ = ["FakeCreatureData"]

fake = Faker()


class FakeCreatureData:
    def __init__(self, count: int = 20):
        self.__count = count
        self.__creatures: list[Creature] = [
            Creature(**self._get_fake_creature())
            for _ in range(self.__count)
        ]

    def _get_fake_creature(self) -> dict[str, str]:
        return {
            "name": fake.first_name(),
            "country": fake.country_code(),
            "area": fake.name(),
            "description": fake.text(100),
            "aka": fake.first_name(),
        }

    def list(self) -> list[Creature]:
        """Список существ."""
        return self.__creatures

    def get(self, name: str) -> Creature | None:
        """
        Получение существа по имени.

        :param name: Имя существа.
        :return: None, если существо не найдено.
        """
        for creature in self.__creatures:
            if creature.name.lower() == name.lower():
                return creature
        return

    def create(self, creature: Creature) -> Creature:
        """Создание нового существа."""
        # new_creature: Creature = Creature(**self._get_fake_creature())
        # self.__creatures.append(new_creature)
        # return new_creature

        return creature

    def modify(self, creature: Creature) -> Creature:
        """Частичное изменение записи существа."""
        return creature

    def replace(self, creature: Creature) -> Creature:
        """Полная замена записи существа."""
        return creature

    def delete(self, name: str) -> None:
        """
        Удаление записи существа.
        :return: None, если запись существовала.
        """
        return


if __name__ == "__main__":
    fake_creature = FakeCreatureData()

    for creature in fake_creature.list():
        print(f"{creature.name} | {creature.country}")
