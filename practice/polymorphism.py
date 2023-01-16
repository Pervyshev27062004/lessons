class Parent:
   def do_something(self):
       print("Class parent")


class Child(Parent):
   def do_something(self):
       print("Class child")
       super().do_something()

c = Child()
c.do_something()

