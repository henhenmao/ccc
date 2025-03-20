
from itertools import groupby

def aaaaaa():
    n = int(input())
    
    def inBounds(x):
        if x < 0 or x >= n:
            return False
        return True

    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]

    # this entire part is to see if it is possible or not
    bnew = [i for i, _ in groupby(b)]

    bpointer = 0
    yes = False
    for i in range(len(a)):
        if bnew[bpointer] == a[i]:
            bpointer += 1
            if bpointer >= len(bnew):
                yes = True
                print("YES")
                break
    if not yes:
        print("NO")
        return # stop program if not possible
    
    # actual swiping part
    # find root indexes
    # find the elements that still are aligned
        # those elements were swiped last


    acount = {}
    bcount = {}
    for i in a:
        if i in acount:
            acount[i] += 1
        else:
            acount[i] = 1
    for i in b:
        if i in bcount:
            bcount[i] += 1
        else:
            bcount[i] = 1

    count = 0


    swipes = []
    previousrootspace = ["hello"]
    while count <= n:

        print(f"ITERATION {count+1} --- {bcount}")
        print(b)
        print()


        rootspace = []
        for i in range(n):
            if a[i] == b[i] and acount[a[i]] != bcount[b[i]]:
            # if a[i] == b[i]:
                rootspace.append(i)
        # if rootspace == previousrootspace:
        #     break
        # previousrootspace = rootspace


        for i in rootspace:
            root = a[i]
            p1 = i-1
            p2 = i+1
            leftcount = 0
            rightcount = 0


            
            while inBounds(p1) and b[p1] == root:
                leftcount += 1

                bcount[b[p1]] -= 1
                if a[p1] not in bcount:
                    bcount[a[p1]] = 1
                else:
                    bcount[a[p1]] += 1

                b[p1] = a[p1]
                

                p1 -= 1
            while inBounds(p2) and b[p2] == root:
                rightcount += 1

                bcount[b[p2]] -= 1
                if a[p2] not in bcount:
                    bcount[a[p2]] = 1
                else:
                    bcount[a[p2]] += 1

                b[p2] = a[p2]
                p2 += 1

            l1 = p1+1
            r1 = i
            l2 = i
            r2 = p2-1
            if l1 != r1:
                swipes.append(["L", l1, r1])
            if l2 != r2:
                swipes.append(["R", l2, r2])

        print("after")
        print(f"rootspace: {rootspace}")
        print(f"a: {str(a)}")
        print(f"b: {str(b)}")
        print()

        count += 1
     
    print(len(swipes))
    for swipe in swipes[::-1]:
        print(" ".join([str(i) for i in swipe]))

aaaaaa()




