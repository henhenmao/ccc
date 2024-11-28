

n = int(input())
gold = True
count = 0
for _ in range(n):
    score = 5*int(input()) - 3*int(input())
    if score <= 40:
        gold = False
    else:
        count += 1

print(f"{count}+") if gold else print(count)
