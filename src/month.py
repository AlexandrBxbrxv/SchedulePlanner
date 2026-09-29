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
    month_name: str
    recorded: list

    def __init__(self, year, month_ind, schedule, first_day=1, last_shift=0):
        self.__year = year
        self.__month_ind = month_ind
        month_names_list = ['ЯНВ', 'ФЕВ', 'МАР', 'АПР', 'МАЙ', 'ИЮН', 'ИЮЛ', 'АВГ', 'СЕН', 'ОКТ', 'НОЯ', 'ДЕК']
        self.month_name = month_names_list[self.__month_ind - 1]
        self.schedule = schedule
        self.first_day = first_day
        self.days_list = []
        self.last_shift = last_shift
        self.recorded = []

    def __repr__(self):
        """Представление для отладки"""
        return f'{self.__class__.__name__}({self.__year}, {self.__month_ind}, "{self.schedule}")'

    def __str__(self):
        """Строковое представление для пользователя"""
        return f'{self.month_name}({self.__month_ind}), Дней: {len(self.days_list)}, "{self.schedule}"'

    def gen_day_list(self):
        """Создает список пустых(только дата) дней и складывает их в список"""
        month_len = calendar.monthrange(self.__year, self.__month_ind)[1]
        day = 1
        name = ''
        while range(month_len):
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
        """Находит день по дате и месяцу(12.06), возвращает на него ссылку"""
        for day in self.days_list:
            if day.date[:5] == date:
                return day

    def find_all_days_off_in_weekdays(self):
        """Возвращает список всех выходных дней выпадающих на будние дни недели"""
        weekdays_dayoffs = []
        if self.schedule == '1/1':
            for day in self.days_list:
                if day.weekday_ind < 5 and day.work_type in ('Выходной', 'Ночная'):
                    weekdays_dayoffs.append(day)
        else:
            for day in self.days_list:
                if day.weekday_ind < 5 and day.is_work is False:
                    weekdays_dayoffs.append(day)
        return weekdays_dayoffs

    def save(self):
        """Записывает сохраненные в формате словарей дни в список"""
        for day in self.days_list:
            day.save()
            self.recorded.append({day.date: day.recorded})

    def load(self, data):
        """В уже созданный пустой график загружает ранее сохраненные данные"""
        index = 0
        for day in self.days_list:
            # Звездочка убирает "dict_values([])" выдает чистые значения в формате словаря
            day.load(*data.values())
            index += 1

    def calculate_schedule(self):
        """ Выбирает и использует метод расчета в зависимости от графика(Например: '5/2') """
        if not self.days_list:
            self.gen_day_list()
        # [self.first_day - 1:] нужно писать во всех методах расчета, нужен для расчета графика с определенного дня
        if self.schedule == '5/2':
            self.__five_two()
        if self.schedule == '1/1':
            self.__one_one()
        if self.schedule == '2/2':
            self.__two_two()

    def __five_two(self):
        """ Метод для расчета графика '5/2' """
        for day in self.days_list[self.first_day - 1:]:
            if day.weekday_ind > 4:
                day.is_work = False
            else:
                day.is_work = True
                day.work_type = 'Дневная'

    def __one_one(self):
        """ Метод для расчета графика '1/1' """
        schedule = ['2', 'В', '1', 'В']
        schedule_index = self.last_shift
        for day in self.days_list[self.first_day - 1:]:
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

    def __two_two(self):
        """ Метод для расчета графика '2/2' """
        schedule = ['2', '2', 'В', 'В']
        schedule_index = self.last_shift
        for day in self.days_list[self.first_day - 1:]:
            index = schedule[schedule_index]
            if index == '2':
                day.is_work = True
                day.work_type = 'Дневная'
            else:
                day.is_work = False
                day.work_type = 'Выходной'

            self.last_shift = schedule_index
            schedule_index += 1
            if schedule_index >= 4:
                schedule_index -= 4


if __name__ == '__main__':
    month = Month(2024, 7, '1/1', 1, 3)  # начиная с 4 дня с ночной смены
    month.calculate_schedule()
    print(month)
    month.save()
    print(month.recorded)
    # for day in month.days_list:
    #     print(day)

    # tes = [{'01.07.2024': {'date': '01.07.2024', 'weekday_int': 0, 'weekday': 'ПН', 'is_work': False, 'work_type': 'Выходной', 'is_vacation': False, 'plans_for_the_day': 'Ничего не запланировано', 'weather': 'Не известно'}}, {'02.07.2024': {'date': '02.07.2024', 'weekday_int': 1, 'weekday': 'ВТ', 'is_work': True, 'work_type': 'Дневная', 'is_vacation': False, 'plans_for_the_day': 'Ничего не запланировано', 'weather': 'Не известно'}}]
    # print(*tes[0].values())
