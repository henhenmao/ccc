

def inBounds(c, col):
    if col >= c or col < 0:
        return False
    return True

# just count all adjacent tiles for each traingle and thats literally it

c = int(input())
row1 = [int(i) for i in input().split()]
row2 = [int(i) for i in input().split()]

count = 0

for i in range(c):
    if i % 2 == 0:
        upwards = True
    else:
        upwards = False

    # check two sides same row first
    if row1[i] == 1:
        count += 3
        if inBounds(c, i-1) and row1[i-1] == 1:
            count -= 1
        if inBounds(c, i+1) and row1[i+1] == 1:
            count -= 1
    
        # check bottom triangle only if upwards
        if upwards and row2[i] == 1:
            count -= 1

for i in range(c):
    if i % 2 == 0:
        upwards = True
    else:
        upwards = False


    if row2[i] == 1:
        count += 3
        # check two sides same row first
        if inBounds(c, i-1) and row2[i-1] == 1:
            count -= 1
        if inBounds(c, i+1) and row2[i+1] == 1:
            count -= 1
        
        # check bottom triangle only if upwards
        if upwards and row1[i] == 1:
            count -= 1


print(count)



