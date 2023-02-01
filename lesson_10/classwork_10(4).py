def generator(power: int, limit: int):
    for current in range(1, limit + 1):
        yield current + power

if __name__ == "__main__":
    my_gen = generator(power = 2, limit = 6)
    print(next(my_gen))
    print(next(my_gen))
    print(next(my_gen))
    print(next(my_gen))
    print(next(my_gen))
    print(next(my_gen))



