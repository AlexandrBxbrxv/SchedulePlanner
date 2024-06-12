def test_month1_init(may):
    assert may.year == 2024
    assert may.month_ind == 5


def test_month2_init(june):
    assert june.year == 2024
    assert june.month_ind == 6


def test_one_one(june_one_one):
    assert june_one_one.days_list[0].is_work is True
    assert june_one_one.days_list[1].is_work is False
    assert june_one_one.days_list[2].is_work is True
    assert june_one_one.days_list[3].is_work is False
