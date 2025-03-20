


d = int(input())
e = int(input())

for _ in range(e):
    a = input()
    b = int(input())
    if a == "+":
        d += b
    else:
        d -= b

print(d)