import math

def nextprime():
    n = int(input())
    prime = -1

    if n <= 1:
        return 2

    while True:
        isprime = True
        sq = math.floor(math.sqrt(n))+1
        for i in range(2, sq):
            if n/i == int(n/i):
                isprime = False
        if isprime:
            prime = n
            break
        n += 1
    return prime


print(nextprime())