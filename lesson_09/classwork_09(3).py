"""
Создать метод, который выводит на экран отформатированное время (HH:MM:SS).
"""
class MyTime:
    def __init__(self, hours, minutes, seconds):
        self.hours, self.minutes, self.seconds = hours, minutes, seconds
        self.timestamp = seconds + minutes * 60 + hours * 60 * 60
    def __repr__(self):
        return f"MyTime: {self.timestamp}"

    def __str__(self):
        return f"MyTime: {self.hours, self.minutes, self.seconds}"

if __name__ == "__main__":
    time = MyTime(10, 12, 10)
    print(time)