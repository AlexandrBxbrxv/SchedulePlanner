import pytest
from src.day import *
from src.month import *


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
def may():
    return Month(2024, 5, '1/1')


@pytest.fixture
def june_one_one():
    june = Month(2024, 6, '1/1')
    june.gen_day_list()
    june.one_one()
    return june
