from random import sample
my_dict = {
    "Belarus": "Gomel",
    "Germany": "Berlin",
    "Ukraine": "Soledar"
}
new_list = list(my_dict.items())
random = sample(new_list, 1)
print(random)

from random import choice

dct = {'1': 'один', '2': 'два', '3': 'три'}
data = choice(list(dct.items()))
print(data)