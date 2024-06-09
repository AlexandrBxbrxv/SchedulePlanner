from src.day import Day
from src.count_method import *
import calendar


class Month:
    """Генерирует и записывает список дней, дни в списке можно изменять после генерации. Функции: расчёт графика работы
    в зависимости от графика(1/1), поиск дней по дате, определение последней смены для перехода на след.
     месяц если нужен, вывод графика в консоль"""

    year: int
    month_ind: int
    schedule: str
    days_list: list
    first_day: int
    last_shift: int

    def __init__(self, year, month_ind, schedule, first_day=1):
        self.year = year
        self.month_ind = month_ind
        self.schedule = schedule
        self.first_day = first_day
        self.days_list = []
        self.last_shift = 0

    def gen_day_list(self):
        """Создает список пустых(только дата) дней и складывает их в список"""
        month_len = calendar.monthrange(self.year, self.month_ind)[1]
        day = 1
        while range(month_len):
            # Добавление 0 в дату если 1-9 станет 01-09
            null_day = ''
            if day < 10:
                null_day = 0

            null_month = ''
            if self.month_ind < 10:
                null_month = 0

            date = f'{null_day}{day}.{null_month}{self.month_ind}.{self.year}'
            self.days_list.append(Day(date))

            day += 1
            month_len -= 1

    def print_day_list(self):
        """Вывод всех дней из списка в консоль, для отладки"""
        for day in self.days_list:
            print(day.short_date())

    def find_day(self, date: str):
        """Находит день, возвращает на него ссылку НО как с ней взаимодействовать после нахождения не ясно - узнать"""
        for day in self.days_list:
            if day.short_date() == date:
                return day.date

    def calculate_schedule(self):
        """Рассчитывает график смен в зависимости от графика"""
        pass


if __name__ == '__main__':
    june = Month(2024, 6, '1/1')
    june.gen_day_list()
    day = june.days_list[7]
    print(day.is_work, day.weekday)
    june.calculate_schedule()
    print(day.is_work, day.weekday)
