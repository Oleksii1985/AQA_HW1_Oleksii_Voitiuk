import pytest

from homework_16.human import Human


def test_human_is_grow_up(human):
    human.grow()

    assert human.age == 37


def test_human_is_dead(dead_human):
    dead_human.grow()

    assert dead_human._Human__status == "dead"


def test_human_is_alive(human):
    # well this step is excessive since return only true or false
    # but if I will change conditions of fixture it will fail with Exception error

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
    # will be better to use monkey patch here
    assert human_without_gender.gender == expected


def test_human_change_gender_exception(human):
    with pytest.raises(Exception):
        human.change_gender("")


def test_validate_gender_exception(human):
    with pytest.raises(Exception):
        human._Human__validate_gender("")
