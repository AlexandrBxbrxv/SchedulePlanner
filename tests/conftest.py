import pytest

from src.day import Day
from src.month import Month
from src.planner import Planner


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
def day_4():
    day = Day('13.06.2024', False, False)
    return day


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


@pytest.fixture
def schedule_1():
    return Planner(2024, 1/1, [6, 7], 1)


@pytest.fixture
def search_date_list_1():
    """Попробуй сделать поиск так: вводишь список 12.06 - 02.07
    ищет сначала месяц, внутри него дни и по порядку складывает их в [] затем повторяет для следующего месяца"""
    return '12.06 - 16.06'


@pytest.fixture
def search_date_list_2():
    return '12.06 - 02.07'
