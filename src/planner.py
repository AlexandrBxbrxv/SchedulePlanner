import json

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
    first_day: int
    recorded: list

    def __init__(self, year, schedule, month_list=None, first_day=1, last_shift=0):
        if month_list is None:
            month_list = range(1, 13)
        self.year = year
        self.month_list = month_list
        self.generated_list = []
        self.schedule = schedule
        self.first_day = first_day
        self.last_shift = last_shift
        self.recorded = []

    def generate_schedule(self):
        """Создает график на список месяцев или на год"""
        for month_id in self.month_list:
            month = Month(self.year, month_id, self.schedule, self.first_day, self.last_shift)
            month.calculate_schedule()
            self.generated_list.append(month)

    def print_schedule(self):
        """Выводит созданный график в консоль"""
        for month in self.generated_list:
            print(month)
            for day in month.days_list:
                print(day)

    def find_day(self, search_date: str):
        """Находит день по дате и месяцу(12.06), возвращает на него ссылку"""
        for month in self.generated_list:
            return month.find_day(search_date)

    def change_for_everything(self, change):
        for month in self.generated_list:
            for day in month.days_list:
                day.plans_for_the_day = change

    def save(self):
        """Запускает рекурсивное сохранение и записывает результат в data.json"""
        for month in self.generated_list:
            month.save()
            self.recorded.append({month.month_name: month.recorded})

        with open('data.json', 'wt', encoding='UTF-8') as file:
            file.write(json.dumps(self.recorded))

    def load(self):
        with open('data.json', 'rt', encoding='UTF-8') as file:
            data = json.loads(file.read())
        index = 0
        for month in self.generated_list:
            month.load(data[index].values())
            index += 1


if __name__ == '__main__':
    my_schedule = Planner(2025, '1/1', [2], 3)
    my_schedule.generate_schedule()
    my_schedule.print_schedule()

    """Попробуй сделать поиск так: вводишь список 12.06 - 02.07
    ищет сначала месяц, внутри него дни и по порядку складывает их в [] затем повторяет для следующего месяца
    [дата_1:дата_2]"""

# with open('data.json', 'rt', encoding='UTF-8') as file:
#     data = json.loads(file.read())
# print(data)
# print(data[0].values())
