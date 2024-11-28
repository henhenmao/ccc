def inBounds(x, y):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    return True

'''
notes:
- set a node as visited at the same time at you are adding the node to the queue
- if you only add a node n as visited when you encounter it,
- there can be many nodes that each add n to the queue since it hasn't been set as visited yet


im going to go insane
i wish i were smart and intelligent
im worthless

DO NOT ASSUME THAT THE INPUT IS A SQUARE (n == m)
DO NOT DOUBLE FOR LOOP 
FOR I IN RANGE(LEN(GRID))
FOR J IN RANGE(LEN(GRID))
DOUBLE FOR LOOP WITH n and m
I REPEAT DO NOT WASTE 3 HOURS OF YOUR LIFE BECAUYSE OF THIS AGAIN

1. get the input
2. create essential variables (grids, visited, camera, directions)
3. initialize the visited grid
    - walls are -1, conveyors are -1, start is -1, all (.)s are 0
4. initialize the camera grid
    a) create a fucntion for valid move (don't go out of bounds)
    b) loop through the grid (double for loop)
    c) for each encountered camera: list down every surrouding cell and mark as camera watched
    d) remember that walls stop the line of sight
    e) cameras cannot see conveyors but can see past them
5. create the functions for valid move and stuff
    a) create a valid move function that checks for the following (for cell = next cell)
        i) is cell out of bounds?
        ii) is cell a wall or start node (cell on visited == -1)
        iii) is cell a conveyor (cell == -2)?
        iv) is cell being watched by a camera (cell on camera == True)
6. bfs using queue and valid move


'''

# getting input type shit
n, m = [int(i) for i in input().split()]
grid = []
for _ in range(n):
    grid.append(list(input()))

directions = ((1,0), (0,1), (-1,0), (0,-1))
conveyors = ("L", "R", "U", "D")
visited = [[-1 for _ in range(m)] for _ in range(n)]

# setting up the visited array
for i in range(n):
    for j in range(m):
        if grid[i][j] == ".":
            visited[i][j] = 0
        elif grid[i][j] == "S":
            start = (i, j, 0)
        # elif grid[i][j] in conveyors:
        #     visited = -1 # AAAAAAA

spawnkill = False
cameragrid = [[False for _ in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        if grid[i][j] == "C":
            for d in directions:
                temp_x, temp_y = i, j
                while inBounds(temp_x, temp_y):
                    if grid[temp_x][temp_y] == "W":
                        break
                    elif grid[temp_x][temp_y] in conveyors:
                        continue
                    elif grid[temp_x][temp_y] == "S":
                        spawnkill = True
                    elif grid[temp_x][temp_y] == ".":
                        cameragrid[temp_x][temp_y] = True

                    temp_x += d[0]
                    temp_y += d[1]


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

def conveyorMove(x, y):
    if x < 0 or y < 0 or x >= n or y >= m: # out of bounds error prevention
        return False
    if visited[x][y] > 0:
        return False
    if grid[x][y] == "L":
        return conveyorMove(x, y-1)
    if grid[x][y] == "R":
        return conveyorMove(x, y+1)
    if grid[x][y] == "U":
        return conveyorMove(x-1, y)
    if grid[x][y] == "D":
        return conveyorMove(x+1, y)
    if grid[x][y] == "W" or grid[x][y] == "S" or grid[x][y] == "C":
        return False
    if cameragrid[x][y]:
        return False
    return [x, y]
    
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
        # print(f"current: ({curr_x} {curr_y})", end=" ")

        # put new paths into queue
        for d in directions:
            # print("interation", end=" ")
            next_x = curr_x+d[0]
            next_y = curr_y+d[1]
            if grid[next_x][next_y] in conveyors:
                temp_conveyor = conveyorMove(next_x, next_y)
                if temp_conveyor:
                    queue.append((temp_conveyor[0], temp_conveyor[1], curr_distance+1))
                    visited[temp_conveyor[0]][temp_conveyor[1]] = curr_distance+1
            elif validMove(next_x, next_y):
                queue.append((next_x, next_y, curr_distance+1))
                visited[next_x][next_y] = curr_distance+1
        # print()



# for i in grid:
#     print(i)
# for i in visited:
#     print(i)
# for i in cameragrid:
#     print(i)
# print()

bfs()
# for i in grid:
#     print(i)
# for i in visited:
#     print(i)


for i in visited:
    for j in i:
        if j != -1:
            print(-1) if j == 0 else print(j)