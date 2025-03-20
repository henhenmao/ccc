
def goodsamples():
    n, m, k = [int(i) for i in input().split()]

    kleft = k-1
    res = [1]
    lastsample = [1]
    index = 1
    new = 1
    encounter = {1:0}

    if (n-1)*2 < kleft or kleft < (n-1):
        return -1
    
    while len(res) < n:
        nleft = n-len(res)
        targetk = kleft-nleft
        
        if kleft == 0:
            return " ".join([str(i) for i in res])
        elif kleft < 0:
            return "bad"

        # goal is to reach a point where you kleft = nleft
        # check if your operation leads to equalling nleft

        if nleft == kleft:
            next = res[-1]
            kleft -= 1

        elif kleft - (len(lastsample)+1) >= nleft-1: # new unfamiliar number
            next = new+1
            if next >= m:
                return -1
            new += 1
            kleft -= len(lastsample)+1

        elif targetk <= len(lastsample):
            next = lastsample[-kleft]
            kleft -= targetk
            lastsample = res[encounter[next]+1:]

        encounter[next] = index
        lastsample.append(next)
        res.append(next)
        index += 1
    return " ".join([str(i) for i in res])


print(goodsamples())


