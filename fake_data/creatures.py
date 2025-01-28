from faker import Faker

from models import Creature

__all__ = ["get_creatures"]

fake = Faker()


def get_fake_data_for_creatures() -> dict[str, str]:
    return {
        "name": fake.first_name(),
        "country": fake.country_code(),
        "area": fake.name(),
        "description": fake.text(100),
        "aka": fake.first_name(),
    }


def get_creatures(count: int = 20) -> list[Creature]:
    return [
        Creature(**get_fake_data_for_creatures())
        for _ in range(count)
    ]


if __name__ == "__main__":
    for creature in get_creatures():
        print(f"{creature.name} | {creature.country}")
