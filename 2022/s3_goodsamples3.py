


def goodsamples():
    n, m, k = [int(i) for i in input().split()]

    n -= 1
    k -= 1
    res = [1]
    lastsample = [1]
    curr = 1
    newnum = 1
    visited = {1:0} # key - number, value - index

    if n > k:
        return -1

    while n > 0:
        if k == n:
            next = res[-1]
            k -= 1
            lastsample = [next]

        elif len(res) >= 2 and res[-1] == res[-2]:
            if res[-1] != 1:
                next = 1
            else:
                next = 2
                if 2 >= m:
                    return -1
                if 2 > newnum:
                    newnum = 2
            k -= 2
            lastsample = [next]
        
        elif k <= len(lastsample):
            next = lastsample[-k]
            k = 0
            lastsample = res[visited[next]+1:]
        
        elif k - (len(lastsample)+1) >= n-1:
            next = newnum+1
            newnum += 1
            if newnum > m:
                return -1
            k -= len(lastsample)+1
            lastsample.append(next)

        else:
            next = res[-1]
            k -= 1
            lastsample = [next]

        visited[next] = curr
        res.append(next)
        curr += 1
        n -= 1
    return " ".join([str(i) for i in res])

print(goodsamples())