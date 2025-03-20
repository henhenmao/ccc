
def walkingSum(c): # gets the total walking sum of a concert postion c
    s = 0
    for friend in friends:
        walk = abs(c-friend[0]) - friend[2]
        if walk > 0:
            s += walk * friend[1]
    return s

friends = []

n = int(input())
low = 10000000000
high = -1

for i in range(n):
    temp = [int(i) for i in input().split()]
    friends.append(temp)

    if temp[0] > high:
        high = temp[0]
    if temp[0] < low:
        low = temp[0]

# print(friends)
# print(low)
# print(high)


# looping through from the min to the max and checking one by one 
# for c in range(low, high+1):
#     temp = walkingSum(c)
#     if temp < min_walk:
#         min_walk = temp

temp = 0

# binary search for the min
while low <= high:
    mid = (low+high)//2
    temp = walkingSum(mid)
    templeft = walkingSum(mid-1)
    tempright = walkingSum(mid+1)

    if temp < templeft and temp < tempright:
        break

    if temp == templeft and temp == tempright:
        break
        
    if temp < tempright:
        high = mid - 1

    elif temp < templeft:
        low = mid + 1

print(temp)