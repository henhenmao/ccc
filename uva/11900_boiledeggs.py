
t = int(input())
for case in range(1, t+1):
    n, p, q = [int(i) for i in input().split()]
    eggs = sorted([int(i) for i in input().split()])

    num_eggs = 0
    weight = 0
    for egg in eggs:
        weight += egg
        num_eggs += 1
        if weight > q or num_eggs > p:
            num_eggs -= 1
            break


    print(f"Case {case}: {num_eggs}")

