class Car:
    brand = None
    model = None
    year = None
    speed = 0
    def __init__(self, brand, model, year, speed):
        self.brand, self.model, self.year, self.speed = brand, model, year, speed

    def acceleration(self):
        print(f"{self.speed + 5} was accelerated")

    def braking(self):
        print(f"{self.speed - 5} was broken")

    def stop(self):
        print(f"{self.speed * 0} was stopped")

    def back(self):
        print(f"{self.speed * (-1)} was turned back")

if __name__ == "__main__":
    car = Car("Volkswagen", "Golf II", 1990, 10)
    car.back()