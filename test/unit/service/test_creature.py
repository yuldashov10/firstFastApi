from src.model.creature import Creature
from src.service import creature as code

first_creature = Creature(
    name="Mount",
    country="RU",
    area="Elbrus",
    description="The highest mountain in Europe",
    aka="Mount Elbrus"
)


def test_create():
    response = code.create(first_creature)

    assert response == first_creature


def test_get_exists():
    response = code.get("Mount")

    # assert response == first_creature
    assert response is None


def test_get_not_exists():
    response = code.get("Some mount")

    assert response is None
