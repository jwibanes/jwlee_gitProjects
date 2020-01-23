#Clock Exercise

class Counter:
    """
    This class is used to present hour, minute, second instances of the class Clock
    """

    def __init__(self, limit):
        """
        Set instance variable limit(max number), value(value counted until now)
        When creating instance, take limit is parameter, and initialize value as 0
        """
        self.limit = limit
        self.value = 0

    def set(self, new_value):
        """
        If parameter >= 0 and parameter < limit, set value as parameter (new_value)
        If not, set self.value as 0
        """
        self.value = new_value if 0 <= new_value < self.limit else 0

    def tick(self):
        """
        increase value by 1
        If class Counter's value reaches limit, change value to 0 and return True
        is class Counter's value is smaller then limit, return False
        """
        self.value += 1

        if self.value == self.limit:
            self.value = 0
            return True
        return False

    def __str__(self):
        """
        return value as a double digit format string type using .zfill
        """
        return str(self.value).zfill(2)


class Clock:
    """
    class Clock
    """
    HOURS = 24  # Maximum of hour
    MINUTES = 60  # Maximum of minute
    SECONDS = 60  # MAximum of second

    def __init__(self, hour, minute, second):
        """
        Define 3 instances (hour, minute, second) and set them using parameter values
        3 Counter instances are created here
        """
        self.hour = Counter(Clock.HOURS)
        self.minute = Counter(Clock.MINUTES)
        self.second = Counter(Clock.SECONDS)

        self.set(hour, minute, second)

    def set(self, hour, minute, second):
        """Set current time as parameter 'hour',  parameter 'minute',  parameter 'second'"""
        # 코드를 쓰세요
        self.hour.set(hour)
        self.minute.set(minute)
        self.second.set(second)

    def tick(self):
        """
        Increase Counter(Clock.SECONDS).value by 1
        If Counter(Clock.SECONDS).value reaches limit, set to 0 and increase Counter(Clock.MINUTES).value by 1
        If Counter(Clock.MINUTES).value also reaches limit, set to 0 and Counter(Clock.HOURS).value by 1
        If Counter(Clock.SECONDS).value also reaches limit, 23 is turned to 00, and 00:00:00 is set
        """
        if self.second.tick():
            if self.minute.tick():
                self.hour.tick()


    def __str__(self):
        """
        Return current time in the format H:M:S
        Example: "03:11:02"
        """
        return "{}:{}:{}".format(self.hour, self.minute, self.second)


#Check whether minute increases when second becomes 60
print("Set time as 01:30:48")
clock = Clock(1, 30, 48)
print(clock)

#Increase 13 seconds
print("13 seconds have passed")
for i in range(13):
    clock.tick()
print(clock)

#Check whether hour increases when minute becomes 60
print("Set time as 02:59:58")
clock.set(2, 59, 58)
print(clock)

#Increase 5 seconds
print("5 seconds have passed")
for i in range(5):
    clock.tick()
print(clock)

#Check whether time is set to 00:00:00 when hour becomes 24
print("Set time as 23:59:57")
clock.set(23, 59, 57)
print(clock)

#Increase 5 seconds
print("5 seconds have passed")
for i in range(5):
    clock.tick()
print(clock)