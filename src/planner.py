from src.month import Month


class Planner:
    """Класс для расчета графика смен на несколько месяцев или на год"""
    # Именно через него и будут производиться все операции и взаимодействие с созданными списками дней внутри месяцев
    # можно будет выставить себе отпуск, изменить график вручную, настроить планы на день

    month_list: list
    schedule: str
    year: int
    generated_list: list
    last_shift: int

    def __init__(self, year, schedule, month_list=None, last_shift=0):
        if month_list is None:
            month_list = range(1, 13)
        self.year = year
        self.month_list = month_list
        self.generated_list = []
        self.schedule = schedule
        self.last_shift = last_shift

    def generate_schedule(self):
        for month in self.month_list:
            the_month = Month(self.year, month, self.schedule, last_shift=self.last_shift)
            the_month.calculate_schedule()
            self.generated_list.append(the_month)

    def print_schedule(self):
        for m in self.generated_list:
            print(m)
            for d in m.days_list:
                print(d)

    def find_day(self, search_date: str):
        """Находит день по дате и месяцу(12.06), возвращает на него ссылку"""
        for month in self.generated_list:
            return month.find_day(search_date)


if __name__ == '__main__':
    my_schedule = Planner(2024, '1/1', [6, 7], 1)
    my_schedule.generate_schedule()
    day = my_schedule.find_day('13.06')
    day1 = my_schedule.find_day('14.06')
    print(day, day1)

    """Попробуй сделать поиск так: вводишь список 12.06 - 02.07
    ищет сначала месяц, внутри него дни и по порядку складывает их в [] затем повторяет для следующего месяца"""
