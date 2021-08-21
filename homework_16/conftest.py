import pytest

from homework_16.human import Human


@pytest.fixture(scope="module")
def human() -> Human:
    yield Human("Alex", 36, "male")


@pytest.fixture(scope="module")
def dead_human() -> Human:
    yield Human("Vasyl", 101, "male")


@pytest.fixture(scope="module")
def human_without_gender() -> Human:
    yield Human("Some", 30, "")
