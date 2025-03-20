
n = int(input())
k = int(input())

total = n
for _ in range(k):
    n *= 10
    total += n
print(total)