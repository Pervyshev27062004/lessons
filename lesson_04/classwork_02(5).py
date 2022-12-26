n = int(input())
m = int(input())
m+=1
result = 0
for i in range(n,m,1):
    count = i ** 3
    print(count)
    result += count
print(result)