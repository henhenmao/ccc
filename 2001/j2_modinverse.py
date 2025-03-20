
x = int(input())
m = int(input())

out = -1
for n in range(1, m+1):
    if (x*n)%m == 1:
        out = n

if out == -1:
    print("No such integer exists.")
else:
    print(out)
