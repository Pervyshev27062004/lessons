if __name__ == "__main__":
    a = int(input())
    b = int(input())
    c = int(input())
    if a % 2 == 0:
        a = a / 2
    else:
        a = a / 2 + 0.5
    if b % 2 == 0:
        b = b / 2
    else:
        b = b / 2 + 0.5
    if c % 2 == 0:
        c = c / 2
    else:
        c = c / 2 + 0.5
    summa = a + b + c
    print("Вот столько парт нам надо:", summa)