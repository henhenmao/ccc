n = int(input())
t = 0
s = 0
for _ in range(n):
    text = input().lower()
    t += text.count("t")
    s += text.count("s")
print("English") if t > s else print("French")