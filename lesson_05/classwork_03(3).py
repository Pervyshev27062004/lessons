#Написать функцию принимающая на вход неопределенным количеством аргументов
# и именованный аргумент func_type. В зависимости от func_type вернуть минимальное
# либо максимальное значение. Написать программу в виде трех функций.
def my_func(*args, func_type):
    if func_type == "min":
        print(func_type)
        return min(args)
    elif func_type == "max":
        return max(args)


my_func(1,2,3,4,5, func_type="min")