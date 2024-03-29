class Car():
    brand = None
    model = None
    year = None
    speed = None

    def __init__(self, brand, model, year, speed):
        self.brand, self.model, self.year, self.speed = brand, model, year, speed

    def accelerate(self):
        print(f"{self.speed + 5} was accelerated")

    def brake(self):
        print(f"{self.speed - 5} was braked")

    def stop(self):
        print(f"{self.speed * 0} was stopped")


if __name__ == "__main__":
    car = Car("Volkswagen", "Golf 2", 1990, 10)
    print(car.brand, car.model, car.year, car.speed)
    car.accelerate()
    car.brake()
    car.stop()

