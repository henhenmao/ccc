
case = 1
while True:
    n = int(input())
    if n == 0:
        break

    jobs = []
    for _ in range(n):
        jobs.append([int(i) for i in input().split()])

    # print(jobs)
    jobs.sort(key=lambda job:-1*job[1])
    # print(jobs)

    time = 0
    leftover = 0
    for job in jobs:
        whole = job[0] + job[1]
        if whole > leftover:
            time += abs(whole-leftover)
            leftover = job[1]
        else:
            leftover = leftover-job[0]
    
    print(f"Case {case}: {time}")
    case += 1
        

