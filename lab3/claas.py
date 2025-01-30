class Time:  
    def __init__(self, second, minut, hours):
        self.second = second
        self.minut = minut
        self.hours = hours
    def __str__(self):
        return "{:02}:{:02}:{:02}".format(self.hours, self.minut, self.second)
    def increment_second(self):
        self.second += 1
        if self.second > 59:
            self.second = 0
            self.increment_minute()
    def increment_minute(self):
        self.minut += 1
        if self.minut > 59:
            self.minut = 0
            self.increment_hour()
    def increment_hour(self):
        self.hours += 1
        if self.hours > 23:
            self.hours = 0
    def decrement_second(self):
        self.second -= 1
        if self.second < 0:
            self.second = 59
            self.decrement_minute()
    def decrement_minute(self):
        self.minut -= 1
        if self.minut < 0:
            self.minut = 59
            self.decrement_hour()    
    def decrement_hour(self):
        self.hours -= 1
        if self.hours < 0:
            self.hours = 23
    def time(self):
        print(self.hours, ":", self.minut, ":", self.second)
t1 = Time(59, 59, 11)
t1.increment_second()
print(t1)