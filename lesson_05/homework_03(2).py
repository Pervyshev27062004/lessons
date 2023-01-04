import random

people = ["ALEX", "sasha", "masha", "maks"]
people = ["ALEX", "sasha", "masha", "maks"]

random.shuffle(people)

for index in range(len(people)):
    if index == len(people) - 1:
        print(f"{people[index]} - {people[0]}")
    else:
        print(f"{people[index]} - {people[index + 1]}")