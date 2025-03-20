

n = int(input())

count = 0

fours = 0
fives = 0
total = 0


while fours*4 <= n:
    if (n-fours*4) % 5 == 0:
        # print(f"fours: {fours}")
        count += 1
    fours += 1

print(count)