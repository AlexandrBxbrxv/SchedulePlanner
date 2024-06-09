def test_day1_init(day1):
    assert day1.date == '09.06.2024'
    assert day1.weekday == 'ВС'
    assert day1.is_work is None
    assert day1.is_vacation is None


def test_day2_init(day2):
    assert day2.is_work is False
    assert day2.is_vacation is None
    assert day2.weekday == 'СБ'


def test_day3_init(day3):
    assert day3.is_work is False
    assert day3.is_vacation
    assert day3.weekday == 'ПН'
