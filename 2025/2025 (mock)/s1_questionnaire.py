


n, m = [int(i) for i in input().split()]

candidates = [[0, i+1] for i in range(m)]

for _ in range(n):
    votes = [int(i) for i in input().split()]
    for i in range(len(votes)):
        if votes[i]:
            candidates[i][0] += 1

candidates.sort(key=lambda x : (-x[0], x[1]))

print(" ".join([str(c[1]) for c in candidates]))