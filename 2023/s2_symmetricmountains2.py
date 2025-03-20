

# i hate this question so much omg

n = int(input())
mountains = [int(i) for i in input().split()]
res = []
min_symmetrys = [1000000000000 for _ in range(n)]



# odd length
for midpoint in range(n):
    p1 = midpoint
    p2 = midpoint+1
    curr_symmetry = 0
    while p1 >= 0 and p2 <= n:
        curr_symmetry += abs(mountains[p2-1]-mountains[p1])
        curr_length = p2-p1
        if curr_symmetry < min_symmetrys[curr_length-1]:
            min_symmetrys[curr_length-1] = curr_symmetry
        p1 -= 1
        p2 += 1

# even length
for midpoint1 in range(n-1):
    midpoint2 = midpoint1+1
    p1 = midpoint1
    p2 = midpoint2+1
    test = mountains[p1:p2]
    curr_symmetry = 0
    while p1 >= 0 and p2 <= n:
        curr_symmetry += abs(mountains[p2-1]-mountains[p1])
        curr_length = p2-p1
        if curr_symmetry < min_symmetrys[curr_length-1]:
            min_symmetrys[curr_length-1] = curr_symmetry
        p1 -= 1
        p2 += 1

print(" ".join([str(i) for i in min_symmetrys]))