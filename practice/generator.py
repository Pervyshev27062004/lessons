from time import sleep


def regular_function():
   result = []
   for i in range(10):
       sleep(0.1)
       result.append(i)
   return result

print(regular_function())
def regular_generator():
   for i in range(10):
       sleep(0.1)
       yield i
print(regular_generator())
