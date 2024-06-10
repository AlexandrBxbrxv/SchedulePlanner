
class CountMethod:
    """
    Пока ХЗ как это сделать, может лучще просто методами класа МЕСЯЦ
    """
    condition: str
    schedule_name: str

    def __init__(self, schedule_name, day):
        self.schedule_name = schedule_name
        self.day = day

    def __call__(self, *args, **kwargs):
        if self.schedule_name == '5/2':
            return self.five_two()

    def five_two(self, **kwargs):
        if self.day.weekday_ind > 4:
            self.day.is_work = False
        else:
            self.day.is_work = True

    def one_one(self, days_list=None):
        if days_list is None:
            days_list = []
        schedule = ['2', 'В', '1', 'В']
        while days_list:
            for day in days_list:
                for ind in schedule:
                    if ind == '2' or ind == '1':
                        day.is_work = True
                    else:
                        day.is_work = False

    def method(self, condition: str):
        if condition == '1/1':
            return self.one_one()
