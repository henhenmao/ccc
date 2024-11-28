
goal, n, rate, day = int(input()), int(input()), int(input()), 0
total = n
while total <= goal:
    n *= rate
    total += n
    day += 1
    # print(str(day) + " " + str(total))
print(day)
