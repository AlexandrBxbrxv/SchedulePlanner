import datetime


class Day:
    """Хранит данные о дне. Функции: устанавливать режим работы и отпуска, записывать планы, узнать погоду"""
    date: str
    weekday: str
    weekday_ind: int
    is_work: bool
    is_vacation: bool
    plans_for_the_day: str
    weather: str
    work_type: str
    recorded: dict

    def __init__(self, date):
        self.date = date
        weekday_ind = datetime.date.weekday(datetime.datetime.strptime(self.date, '%d.%m.%Y'))
        week = ['ПН', 'ВТ', 'СР', 'ЧТ', 'ПТ', 'СБ', 'ВС']
        self.weekday = week[weekday_ind]
        self.weekday_ind = weekday_ind
        self.is_work = False
        self.work_type = 'Выходной'
        self.is_vacation = False
        self.plans_for_the_day = 'Ничего не запланировано'
        self.weather = 'Не известно'
        self.recorded = dict()

        if self.is_work:
            self.is_vacation = False

        if self.is_vacation:
            self.is_work = False

    def __repr__(self):
        return f'{self.__class__.__name__}("{self.date}")'

    def __str__(self):
        return f'{self.date[:2]}|{self.weekday}|{self.work_type}'

    def short_date(self):
        """Возвращает сокращенную до дней дату"""
        result = self.date[:2]
        if int(self.date[:2]) < 10:
            result = self.date[1:2]
        return result

    def write_down(self):
        """Записывает все значения дня в словарь, нужно вызывать после каждого изменения"""
        self.recorded = {
            'date': self.date,
            'weekday_int': self.weekday_ind,
            'weekday': self.weekday,
            'is_work': self.is_work,
            'work_type': self.work_type,
            'is_vacation': self.is_vacation,
            'plans_for_the_day': self.plans_for_the_day,
            'weather': self.weather
        }


if __name__ == '__main__':
    day = Day('13.06.2024')
    day.plans_for_the_day = 'Программировать'
    print(day.recorded)
    day.write_down()
    print(day.recorded)
