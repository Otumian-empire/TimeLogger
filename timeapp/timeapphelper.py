import datetime

class TimeappTime:

    def __init__(self):
        self.hour = datetime.datetime.timetz(datetime.datetime.today()).hour
        self.minute = datetime.datetime.timetz(datetime.datetime.today()).minute
        self.second = datetime.datetime.timetz(datetime.datetime.today()).second

    def get_current_time(self):
        return datetime.time(hour=self.hour, minute=self.minute, second=self.second)


    @staticmethod
    def total_secs():
        total = self.hour * 3600
        total += self.minute * 60
        total += self.second

        return total

    

# x = get_current_time()

# y = get_current_time()

# print(x, y, x - y)

# t = TimeappTime()
# print(t.get_current_time())