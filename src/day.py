import datetime


class Day:
    """Хранит данные о дне. Функции: устанавливать режим работы и отпуска, записывать планы, узнать погоду"""
    date: str
    weekday: str
    weekday_ind: int
    is_work: bool
    is_vacation: bool
    plan: str
    weather: str

    def __init__(self, date, is_work=None, is_vacation=None, plan=None, weather=None,):
        self.date = date
        weekday_ind = datetime.date.weekday(datetime.datetime.strptime(self.date, '%d.%m.%Y'))
        week = ['ПН', 'ВТ', 'СР', 'ЧТ', 'ПТ', 'СБ', 'ВС']
        self.weekday = week[weekday_ind]
        self.weekday_ind = weekday_ind
        self.is_work = is_work
        self.is_vacation = is_vacation
        self.plan = plan
        self.weather = weather

        if self.is_work:
            self.is_vacation = False

        if self.is_vacation:
            self.is_work = False

    def short_date(self):
        """Возвращает сокращенную до дней дату"""
        result = self.date[:2]
        if int(self.date[:2]) < 10:
            result = self.date[1:2]
        return result
