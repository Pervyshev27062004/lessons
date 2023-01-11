def factorial_recursive(n: int) -> int:
   if n == 1:
       return n
   return n + factorial_recursive(n - 1)

print(f"Factorial for 7 == {factorial_recursive(7)}")

class ClassName:
    name = "OOP"
    color = "red"

    def print_name(self):
        print(self.name)

    def print_color(self):
        print(self.color)

my_class = ClassName()
my_class.print_color()

