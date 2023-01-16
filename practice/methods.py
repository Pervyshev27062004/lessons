class Car:
   last_model = None

   def __init__(self, model):
       self.model = model

   @classmethod
   def get_last_model(cls):
       return cls.last_model


Car.last_model = "Opel"

car1 = Car("Toyota")
print(Car.get_last_model())

class Car:
    last_model = None

    def __init__(self, model):
        self.model = model

    @staticmethod
    def is_model_ok(model):
        return len(model) > 5


print(Car.is_model_ok("test"))
