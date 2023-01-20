b = int(input())
m = int(input())
n = int(input())

def generator():
    for i in range(m,n):
        yield i ** b
my_gen = generator()
while True:
    try:
        print(next(my_gen))
    except StopIteration:
        break
print(next(my_gen))
