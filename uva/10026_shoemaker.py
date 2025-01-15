

t = int(input())
for test in range(t):
    a = input()

    jobs = []
    n = int(input())
    for j in range(n):
        temp = [int(i) for i in input().split()]
        temp.append(j+1)
        jobs.append(temp)

    jobs.sort(key=lambda job: -1*(job[1]/job[0]))

    print(" ".join([str(job[2]) for job in jobs]))

    if test < t-1:
        print()