"""
Головоломка “Ханойские башни”
"""
def hanoi(n, i, k):
    if n == 1:
        print(f"Move disk {n} from pin {i} to {k}")
    else:
        tmp = 6 - i - k
        print(hanoi(n-1, i, tmp))
        print(hanoi(n-1, tmp, k))
n = int(input())
hanoi(n, 1, 2)

def move(n, start, finish) :
    if n==1:
        print(n, start, finish)
    else:
         tmp= 6 - start - finish
         move(n - 1, start, tmp)
         print(n, start, finish)
         move(n - 1, tmp, finish)
n=int(input())
move(n, 1, 3)


