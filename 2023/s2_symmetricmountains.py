

n = int(input())
mountains = [int(i) for i in input().split()]
res = []


for length in range(n):
    min_symmetry = 1000000000000
    for i in range(len(mountains)-length):
        count = 0
        p1 = i
        p2 = i+length
        while p1 < p2:
            count += abs(mountains[p1]-mountains[p2])
            p1 += 1
            p2 -= 1
        if count < min_symmetry:
            min_symmetry = count
    res.append(str(min_symmetry))

print(" ".join(res))

