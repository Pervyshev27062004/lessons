import random

my_list = []
x= random.randint(0,4)
print(x,"Zahl")
for i in range(x):
    y= random.randint(0,2)
    my_list.append(y)
    print(y)
    print(my_list)
result = 0
for element in my_list:
    if element >10:
        result += element
print(result)

