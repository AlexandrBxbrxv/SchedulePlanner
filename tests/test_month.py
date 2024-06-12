def test_month1_init(may_5_2):
    assert repr(may_5_2) == 'Month(2024, 5, "5/2")'
    assert may_5_2.schedule == "5/2"


def test_month2_init(june_1_1):
    assert repr(june_1_1) == 'Month(2024, 6, "1/1")'
    assert june_1_1.first_day == 1


def test_five_two(may_5_2):
    assert may_5_2.days_list[0].work_type == 'Дневная'
    assert may_5_2.days_list[1].work_type == 'Дневная'
    assert may_5_2.days_list[2].work_type == 'Дневная'
    assert may_5_2.days_list[3].work_type == 'Выходной'
    assert may_5_2.days_list[4].work_type == 'Выходной'
    assert may_5_2.days_list[5].work_type == 'Дневная'
    assert may_5_2.days_list[6].work_type == 'Дневная'


def test_one_one(june_1_1):
    assert june_1_1.days_list[0].work_type == 'Дневная'
    assert june_1_1.days_list[1].work_type == 'Выходной'
    assert june_1_1.days_list[2].work_type == 'Ночная'
    assert june_1_1.days_list[3].work_type == 'Выходной'


def test_find_day(june_1_1):
    day = june_1_1.find_day('12')
    assert day.is_work is False
    assert day.date == '12.06.2024'

