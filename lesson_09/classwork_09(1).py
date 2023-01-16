"""
Создать класс MyTime. Атрибуты: hours, minutes, seconds. Методы:
 переопределить магические методы сравнения (==, !=, >=, <=, <, >).
"""

from _datetime import datetime
now = datetime.now()
print(now)

class MyTime:
    def __init__(self, hours, minutes, seconds):
        self.hours, self.minutes, self.seconds = hours, minutes, seconds
        self.timestamp = seconds + minutes * 60 + hours * 60 * 60

    def __eq__(self, other) -> bool:
        return (self.timestamp == other.timestamp )
    def __lt__(self, other) -> bool:
        return (self.timestamp < other.timestamp )
    def __ne__(self, other) -> bool:
        return (self.timestamp != other.timestamp)
    def __ge__(self, other) -> bool:
        return self.timestamp >= other.timestamp


if __name__ == "__main__":
    time1 = MyTime(10, 11, 11)
    time2 = MyTime(12, 12, 12)

    print(time1.__eq__(time2))
    print(time1 == time2)  # This is the same
    print(time1.__lt__(time2))
    print(time1.__ne__(time2))
    print("more or eq:",time1.__ge__(time2))





