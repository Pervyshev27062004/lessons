"""
Переопределить магические методы сложения, вычитания, умножения на число.
"""
from __future__ import annotations


class MyTime:
    def __init__(self, hours, minutes, seconds):
        self.hours, self.minutes, self.seconds = hours, minutes, seconds
        self.timestamp = seconds + minutes * 60 + hours * 60 * 60

    def __add__(self, other) -> MyTime:
        timestamp = self.timestamp + self.timestamp
        hours = timestamp // (60 * 60)
        minutes = (timestamp % (60 * 60) // 60)
        seconds = timestamp % 60
        return MyTime(hours, minutes, seconds)

    def __repr__(self):
        return f"MyTime: {self.timestamp}"

    def __str__(self):
        return f"MyTime: {self.hours, self.minutes, self.seconds}"


if __name__ == "__main__":
    time1 = MyTime(10, 1, 11)
    time2 = MyTime(10, 1, 12)
    print(time1.__add__(time2))
    print(time1 + time2)  # this is the same
