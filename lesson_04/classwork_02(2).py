n = int(input("Введите n:"))
result = 0
current = 1
while current <= n:
    result += current ** 3
    current +=1
    print(result)
