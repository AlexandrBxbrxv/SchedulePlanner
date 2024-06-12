from src.month import Month


class Planner:
    """Класс для расчета графика смен на несколько месяцев или на год"""
    # Именно через него и будут производиться все операции и взаимодействие с созданными списками дней внутри месяцев
    # можно будет выставить себе отпуск, изменить график вручную, настроить планы на день

    month_list: list
    schedule: str
    year: int
    generated_list: list

    def __init__(self, year, schedule, month_list=None):
        if month_list is None:
            month_list = range(1, 13)
        self.year = year
        self.month_list = month_list
        self.generated_list = []
        self.schedule = schedule

    def generate_schedule(self):
        for month in self.month_list:
            the_month = Month(self.year, month, self.schedule)
            the_month.calculate_schedule()
            self.generated_list.append(the_month)


if __name__ == '__main__':
    my_schedule = Planner(2024, schedule='1/1')
    my_schedule.generate_schedule()
    for m in my_schedule.generated_list:
        print(m)
        for d in m.days_list:
            print(d)
