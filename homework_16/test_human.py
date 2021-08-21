import pytest

from homework_16.human import Human


def test_human_is_grow_up(human):
    human.grow()

    assert human.age == 37


def test_human_is_dead(dead_human):
    dead_human.grow()

    assert dead_human._Human__status == "dead"


def test_human_is_alive(human):
    human._Human__is_alive()

    assert human._Human__status == "alive"


def test_human_is_alive_exception(dead_human):
    with pytest.raises(Exception):
        dead_human._Human__is_alive()


@pytest.mark.parametrize(
    "gender,expected",
    [("male", "male"), ("female", "female")],
    ids=["change_to_male", "change_to_female"]
)
def test_change_gender(human_without_gender, gender, expected):
    human_without_gender.change_gender(gender)

    assert human_without_gender.gender == expected


def test_human_change_gender_exception(human):
    with pytest.raises(Exception):
        human.change_gender("")


def test_validate_gender_exception(human):
    with pytest.raises(Exception):
        human._Human__validate_gender("")
