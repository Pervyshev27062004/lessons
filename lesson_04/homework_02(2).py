my_str = "А роза упала на лапу Азора"

my_str = my_str.lower().replace("", "")

if my_str == my_str[::-1]:
    print("True")
else:
    print("False")