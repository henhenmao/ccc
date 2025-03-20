    



def loowater(n, m):
    heads = []
    knights = []
    count = 0

    for _ in range(n):
        heads.append(int(input()))
    for _ in range(m):
        knights.append(int(input()))

    heads.sort()
    knights.sort()


    headpointer = 0
    knightpointer = 0

    while knightpointer < len(knights):
        headheight = heads[headpointer]
        knightheight = knights[knightpointer]
        if knightheight >= headheight:
            count += knightheight
            headpointer += 1
        if headpointer >= len(heads):
            return count
        knightpointer += 1

    return "Loowater is doomed!"


    
while True:
    n, m = [int(i) for i in input().split()]
    if n == 0 and m == 0:
        break
    print(loowater(n, m))