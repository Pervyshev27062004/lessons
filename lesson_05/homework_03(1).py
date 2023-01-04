def three_args(var1, var2, var3):
    my_dict = locals()
    print("Переданные данные:", *(f"{var} = {number}" for var, number in my_dict.items() if number))



three_args(1, None, 10)
"""
Для решения задачи используйте функцию locals (), которая в виде словаря представит все внутренние аргументы функции. 
"""

def three_args(var1, var2, var3):
    print(f"Переданные данные: var1 = {var1} var2 = {var2} var3 = {var3}")


three_args( 1, None, 3)