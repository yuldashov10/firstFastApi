import os

import pytest

from core.exceptions import ObjectDoesNotExist, DuplicateRecordError
from src.model.creature import Creature

# set this before data imports below for data.init
os.environ["CRYPТID_SQLIТE_DB"] = ":memory:"

from src.data import creature


@pytest.fixture
def sample() -> Creature:
    return Creature(
        name="yeti",
        country="CN",
        area="Himalayas",
        description="Harmless Himalayan",
        aka="AbominaЫe Snowman"
    )


def test_create(sample):
    resp = creature.create(sample)
    assert resp == sample


def test_create_duplicate(sample):
    with pytest.raises(DuplicateRecordError):
        _ = creature.create(sample)


def test_get_one(sample):
    resp = creature.get(sample.name)
    assert resp == sample


def test_get_one_missing():
    with pytest.raises(ObjectDoesNotExist):
        _ = creature.get("boxturtle")


def test_modify(sample):
    creature.area = "Sesame Street"
    resp = creature.modify(sample.name, sample)
    assert resp == sample


def test_modify_missing():
    new_creature: Creature = Creature(
        name="snurfle",
        country="RU",
        area="",
        description="some thing",
        aka=""
    )
    with pytest.raises(ObjectDoesNotExist):
        _ = creature.modify(new_creature.name, new_creature)


def test_delete(sample):
    resp = creature.delete(sample.name)
    assert resp is None


def test_delete_missing(sample):
    with pytest.raises(ObjectDoesNotExist):
        _ = creature.delete(sample.name)
