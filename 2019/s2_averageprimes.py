import math

# primes = {}
# for i in range(1, 500000): # every number from 1 to half of n (target)
#     # print("number: " + str(i), end=" ")
#     isprime = True
#     for j in range(1, math.floor(math.sqrt(i))+1): # seeing if number is a prime
#         if j != 1 and j != i and i%j == 0:
#             isprime = False
#             break
#     if isprime:
#         primes[i] = i


n = 2000000
primes = [True] * (n+1)
primes[0], primes[1] = False, False
for i in range(2, int(math.sqrt(n))+1): # 2 to square root of n
    if primes[i]: # not checked yet
        for j in range(i*2, n, i):
            primes[j] = False
primes[2000000] = False

a = {}
for i in range(len(primes)):
    if primes[i]:
        a[i] = i
        


# print(primes)
t = int(input())
for _ in range(t):
    n = int(input())*2

    for k in a.keys():
        if n-k in a:
            print(f"{k} {n-k}")
            break

'''
2, 4, 6, ...
3, 6, 9, ...
5, 10, 15...





'''


# 2 ==> 2 is prime
# 4, 6, 8, 10, 12, 14... not prime
# 3 ==> 3 is prime
# 6, 9, 12, ... not prime

# for i in range(len(primes)):
#     if primes[i]:
#         print(i)

'''
- ignore multiple of 2's
- ignore multiple of 3's
- ignore multiple of 5's
- ignore multiple of 7's


144
1,2,3,4,6,8,12,18,24,36,48,72,144

1 * 144
2 * 72
3 * 48
4 * 36
6 * 24
8 * 18
12 * 12


n = 1000000
primes = [True] * n+1
for i in range(2, int(math(sqrt(n)))+1): 2 to square root of n
    for j in range(i, n, i):
        if primes[j]:
            continue
        else:
            primes[j] = False
        




- for each iteration i from 2 to sqrt(1000000) mark every mukltiple of current i as not a prime
    - 2 to sqrt(1000000) - o(n(log(n)))
        - every 
- for each sample input

'''