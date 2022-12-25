n = int(input())
m = int(input())
result = 0
for i in range(n,m,1):
    count = i ** 3
    print(count)
    result += count
print(result)