import math

primes = {}
for i in range(1, 500000): # every number from 1 to half of n (target)
    # print("number: " + str(i), end=" ")
    isprime = True
    for j in range(1, math.floor(math.sqrt(i))+1): # seeing if number is a prime
        if j != 1 and j != i and i%j == 0:
            isprime = False
            break
    if isprime:
        primes[i] = i

# print(primes)
t = int(input())
for _ in range(t):
    n = int(input())*2

    for k in primes.keys():
        if n-k in primes:
            print(f"{k} {n-k}")
            break



