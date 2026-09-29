def test_planner_find_day(schedule_1):
    schedule_1.generate_schedule()
    day = schedule_1.find_day('13.06')
    assert day.date == '13.06.2024'
