import pytest

from homework_16.human import Human


def test_age(human):
    assert human.age == 36


def test_gender(human):
    assert human.gender == "male"


def test_grow_up(human):
    human.grow()

    assert human._Human__age == 37


def test_is_alive(human):
    human._Human__is_alive()

    assert human._Human__status == "alive"


def test_change_gender(human):
    human.change_gender("female")

    assert human._Human__gender == "female"


def test_change_gender_exception(human):
    with pytest.raises(Exception):
        human.change_gender("")


def test_validate_gender_exception(human):
    with pytest.raises(Exception):
        human._Human__validate_gender("")


def test_grow_dead(human, monkeypatch):
    monkeypatch.setattr(
        human, "_Human__age", 101
    )
    human.grow()

    assert human._Human__status == "dead"


def test_is_alive_dead(human):
    with pytest.raises(Exception):
        human._Human__is_alive()
