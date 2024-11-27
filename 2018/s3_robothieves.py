


'''
notes:
- set a node as visited at the same time at you are adding the node to the queue
- if you only add a node n as visited when you encounter it,
- there can be many nodes that each add n to the queue since it hasn't been set as visited yet


im going to go insane
i wish i were smart and intelligent
im worthless
'''


# getting input type shit
n, m = [int(i) for i in input().split()]
grid = []
for _ in range(n):
    grid.append(list(input()))

# loop through this array to simulate all four direction from a given point
directions = ((1,0), (0,1), (-1,0), (0,-1))

visited = [[-1 for _ in range(m)] for _ in range(n)]

# setting up the visited array
for i in range(n):
    for j in range(m):
        if grid[i][j] == ".":
            visited[i][j] = 0
        elif grid[i][j] == "S":
            start = (i, j, 0)

spawnkill = False # in case camera is looking at the spawn point


# simple function that inputs a point on a grid
# outputs whether or not the output is in bounds and won't throw an exception
def inBounds(x, y):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    return True

# loops through the grid and
# for every camera cell found:
# loops for each four directions:
# for each direction, go in a straight line until a wall is encountered or out of bounds
# anything that the loop goes through will turn each (.) cell into a camera watched cell
# if the starting point is encountered:
# you are spawnkilled - everything is a -1
cameragrid = [[False for _ in range(m)] for _ in range(n)]
for i in range(len(grid)):
    for j in range(len(grid)):
        if grid[i][j] == "C":
            for d in directions:
                temp_x, temp_y = i, j
                while inBounds(temp_x, temp_y):
                    if grid[temp_x][temp_y] == "W":
                        break
                    elif grid[temp_x][temp_y] == "S":
                        spawnkill = True
                    elif grid[temp_x][temp_y] == "." or grid[temp_x][temp_y] == "C":
                        cameragrid[temp_x][temp_y] = True

                    temp_x += d[0]
                    temp_y += d[1]

# function similar to inBounds() that checks if a move from a point on the grid is a valid move
# aka "are you able to put this point onto the queue and go on it"
# cell = next cell you are looking at
# if (cell is a wall) or (cell is watched on cameragrid) or (cell value > 0 (visited before))
# then you cannot go on cell and returns False
# else
# you know that it is NOT a wall and NOT watched and NOT visited before
# returns True - adds cell onto the queue and loops onto it
def validMove(x, y):
    if x < 0 or y < 0 or x >= n or y >= m: # out of bounds error prevention
        return False
    if visited[x][y] > 0: # visited (.) node
        return False
    if grid[x][y] == "W" or grid[x][y] == "S" or grid[x][y] == "C": # potential camera watched nodes and walls
        return False
    if cameragrid[x][y]:
        return False
    return True


# bfs algorithm to traverse every possible point on the grid
# for each cell:
# check each cell around it
# view each of the four cells as a possible next point
# if it is a valid move:
# move there
# else skip it
def bfs():
    if spawnkill:
        queue = []
    else:
        queue = [start]
    while queue:
        # get data from the queue pop
        curr = queue.pop(0)
        curr_x, curr_y = curr[0], curr[1]
        curr_distance = curr[2]

        # debug statements
        print(f"current: ({curr_x} {curr_y})", end=" ")

        # put new paths into queue
        for d in directions:
            if validMove(curr_x+d[0], curr_y+d[1]):
                queue.append((curr_x+d[0], curr_y+d[1], curr_distance+1))
                visited[curr_x+d[0]][curr_y+d[1]] = curr_distance+1
        print()


print("-=BEFORE=-")
for i in grid:
    print(i)
for i in visited:
    print(i)
for i in cameragrid:
    print(i)
print()

bfs()

print("-=AFTER=-")
for i in grid:
    print(i)
for i in visited:
    print(i)
print()


for i in visited:
    for j in i:
        if j != -1:
            print(-1) if j == 0 else print(j)

