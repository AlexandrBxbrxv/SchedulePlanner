import pytest

from src.day import Day
from src.month import Month


@pytest.fixture
def day1():
    return Day('09.06.2024')


@pytest.fixture
def day2():
    return Day('08.06.2024', False)


@pytest.fixture
def day3():
    return Day('10.06.2024', is_vacation=True)


@pytest.fixture
def may_5_2():
    may = Month(2024, 5, '5/2')
    may.calculate_schedule()
    return may


@pytest.fixture
def june_1_1():
    june = Month(2024, 6, '1/1')
    june.calculate_schedule()
    return june
