"""
Создать программу, которая импортирует класс из предыдущей задачи,
создает объект и при инициализации устанавливает марку Mercedes,
 модель E500, год выпуска 2000. Далее “разгоняет” машину до 100 км/ч и выводит скорость на экран.
"""
from lesson_08.homework_08 import Car

if __name__ == "__main__":
    S4 = Car("Mercedes", "E500", 2000, 95)

    print(S4.brand, S4.model, S4.year, S4.speed)
    S4.accelerate()
