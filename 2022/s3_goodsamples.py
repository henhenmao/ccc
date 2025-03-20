

def goodsamples():
    n, m, target = [int(i) for i in input().split()]

    target -= 1
    res = [1]

    # first two subtasks: m = 2
    if (n-1)*2 < target or target < (n-1):
        return -1

    while len(res) < n:
        left = n-len(res)
        if left == target:
            next = res[-1]
            target -= 1
        elif left >= target//2:
            if res[-1] == 1:
                next = 2
            else:
                next = 1
            target -= 2
        
        res.append(next)


    return " ".join([str(i) for i in res])


print(goodsamples())


