import pytest

from homework_16.human import Human


@pytest.fixture(scope="module")
def human() -> Human:
    yield Human("Alex", 36, "male")
