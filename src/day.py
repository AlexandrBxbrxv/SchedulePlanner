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
        weekday_ind = datetime.date.weekday(datetime.datetime.strptime(self.date, '%d.%m.%Y').date())
        week = ['ПН', 'ВТ', 'СР', 'ЧТ', 'ПТ', 'СБ', 'ВС']
        self.weekday = week[weekday_ind]
        self.weekday_ind = weekday_ind
        self.is_work = False
        self.work_type = 'Выходной'
        self.is_vacation = False
        self.plans_for_the_day = 'Ничего не запланировано'
        self.weather = 'Не известно'
        self.recorded = dict()

        # В момент инициализации записывает предустановленные значения дня в словарь
        self.save()

        if self.is_work is True:
            self.is_vacation = False

        if self.is_vacation is True:
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

    def save(self):
        """Перезаписывает все значения дня в словарь"""
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

    def load(self, data):
        """Загружает данные из словаря в self"""
        self.date = data['date']
        self.weekday_ind = data['weekday_ind']
        self.weekday = data['weekday']
        self.is_work = data['is_work']
        self.work_type = data['work_type']
        self.is_vacation = data['is_vacation']
        self.plans_for_the_day = data['plans_for_the_day']
        self.weather = data['weather']

    def try_to_get_weather(self):
        """Проверяет, попадает ли дата в диапазон 10 дней от сегодня, если да - автоматически применяет метод
         загрузки погоды с сайта, если нет возвращает строку"""
        today = datetime.datetime.today().date()
        date_dt_format = datetime.datetime.strptime(self.date, '%d.%m.%Y').date()
        today_10 = today + datetime.timedelta(days=10)

        if today <= date_dt_format < today_10:
            self.load_weather()
        else:
            print(f'{self.date} out of predictable range')

    def load_weather(self):
        self.weather = 'weather'
