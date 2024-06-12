from src.day import Day
import calendar


class Month:
    """Генерирует и записывает список дней, дни в списке можно изменять после генерации. Функции: расчёт графика работы
    в зависимости от графика(1/1), поиск дней по дате, определение последней смены для перехода на след.
     месяц если нужен"""

    year: int
    month_ind: int
    schedule: str
    days_list: list
    first_day: int
    last_shift: int

    def __init__(self, year, month_ind, schedule, first_day=1):
        self.__year = year
        self.__month_ind = month_ind
        self.schedule = schedule
        self.first_day = first_day
        self.days_list = []
        self.last_shift = 0

    def __repr__(self):
        return f'{self.__class__.__name__}({self.__year}, {self.__month_ind}, "{self.schedule}")'

    def gen_day_list(self):
        """Создает список пустых(только дата) дней и складывает их в список"""
        month_len = calendar.monthrange(self.__year, self.__month_ind)[1]
        day = self.first_day
        while range(month_len - day):
            # Добавление 0 в дату если 1-9 станет 01-09
            null_day = ''
            if day < 10:
                null_day = 0

            null_month = ''
            if self.__month_ind < 10:
                null_month = 0

            date = f'{null_day}{day}.{null_month}{self.__month_ind}.{self.__year}'
            self.days_list.append(Day(date))

            day += 1
            month_len -= 1

    def find_day(self, date: str):
        """Находит день по короткой дате(1, 9, 31), возвращает на него ссылку"""
        for day in self.days_list:
            if day.short_date() == date:
                return day

    def calculate_schedule(self):
        """ Выбирает и использует метод расчета в зависимости от графика(Например: '5/2') """
        if not self.days_list:
            self.gen_day_list()

        if self.schedule == '5/2':
            self.__five_two()
        if self.schedule == '1/1':
            self.__one_one()

    def __five_two(self):
        """ Метод для расчета графика '5/2' """
        for day in self.days_list:
            if day.weekday_ind > 4:
                day.is_work = False
                day.work_type = 'Выходной'
            else:
                day.is_work = True

    def __one_one(self):
        """ Метод для расчета графика '1/1' """
        schedule = ['2', 'В', '1', 'В']
        schedule_index = self.last_shift
        for day in self.days_list:
            index = schedule[schedule_index]
            if index == '2':
                day.is_work = True
                day.work_type = 'Дневная'
            elif index == '1':
                day.is_work = True
                day.work_type = 'Ночная'
            else:
                day.is_work = False
                day.work_type = 'Выходной'

            self.last_shift = schedule_index
            schedule_index += 1
            if schedule_index >= 4:
                schedule_index -= 4


if __name__ == '__main__':
    june = Month(2024, 1, '1/1', 1)
    june.last_shift = 2
    june.calculate_schedule()
    print(june)
    for day in june.days_list:
        print(day)
    print(june.last_shift)

    # day = june.find_day('12')
    # print(f'{day.date}|{day.weekday}|{day.work_type}\n{day.plan}')
    # day.plan = 'Погулять'
    # print(f'{day.date}|{day.weekday}|{day.work_type}\n{day.plan}')
