

n = int(input())
a = input()
b = input()
count = 0
for i in range(len(a)):
    if a[i] == "C" and a[i] == b[i]:
        count += 1
print(count)