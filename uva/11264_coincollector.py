

# get the number of different coins and the list of coin inputs

t = int(input())
for _ in range(t):
    n = int(input())
    coins = [int(i) for i in input().split()]

    temp = 1
    if len(coins) == 1:
        total = 1
    else:
        total = 2
    
    for i in range(1, len(coins)-1):
        if temp + coins[i] < coins[i+1]:
            temp += coins[i]
            total += 1
    
    print(total)
    