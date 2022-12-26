my_dict = {0: ["123", "243", "345"], 1: ["234", "345", "555", "3"], 2: ["123", "234", "345","3", "66"]}

for index, lst in my_dict.items():
    while True:
        current_symbol = input()
        if current_symbol.isnumeric():
            lst.append(current_symbol)
        else:
            break

all_elements = my_dict[0] + my_dict[1] + my_dict[2]
new_list = []
for element in all_elements:
    if element in my_dict[0] and element in my_dict[1] and element not in my_dict[2]:
        new_list.append(element)


print(new_list)
