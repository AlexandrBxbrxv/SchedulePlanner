def test_day1_init(day1):
    assert day1.date == '09.06.2024'
    assert day1.weekday == 'ВС'
    assert day1.is_work is False
    assert day1.is_vacation is False


def test_day2_init(day2):
    assert day2.is_work is False
    assert day2.is_vacation is False
    assert day2.weekday == 'СБ'
    assert day2.plans_for_the_day == 'Ничего не запланировано'


def test_day3_init(day3):
    assert day3.is_work is False
    assert day3.is_vacation is False
    assert day3.weekday == 'ПН'
    assert day3.weather == 'Не известно'


def test_short_date(day1, day3):
    assert day1.short_date() == '9'
    assert day3.short_date() == '10'


def test_save(day_4):
    day_4.plans_for_the_day = 'Программировать'
    day_4.save()
    assert day_4.recorded == {
        'date': '13.06.2024',
        'weekday_int': 3,
        'weekday': 'ЧТ',
        'is_work': False,
        'work_type': 'Выходной',
        'is_vacation': False,
        'plans_for_the_day': 'Программировать',
        'weather': 'Не известно'
    }
