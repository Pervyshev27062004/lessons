import random
from random import randint
def santa(var1, var2, var3, var4, var7, var8):
    var5 = 0
    var6 = 0
    x = random.randint(1,10)
    print(x)
    if x <= 3:
        var5 = var2
        
    if x > 3 and x <= 6:
        var5 = var3
    if x > 6:
        var5 = var4

    print(f"1 пара: {var1} - {var5} 2 пара: {var3} - {var6} 3 пара: {}")
santa("Alex","Sasha","Masha","Adolf","Josef", "Jesus")