"""
1. get the input
2. create essential variables (grids, visited, camera, directions)
3. initialize the visited grid
    - walls are -1, conveyors are -1, start is -1, all (.)s are 0
    - treat conveyors as a -1 but allow them to be traversed (own separate valid move function?)
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
        iii) is cell a conveyor (cell == -2)? (ignore this part)
        iv) is cell being watched by a camera (cell on camera == True)
    b) if the next move is a conveyor then check if the conveyor leads to a valid move (cell = next cell)
        i) check which direction the conveyor leads to (cell2 = conveyor next cell)
        ii) is cell2 in bounds? - cannot go there
        iii) is cell2 another conveyor? - return recursively
        iv) is cell2 a wall? - cannot go there
        v) is cell2 being watched by a camera? - cannot go there
6. bfs using queue and valid move

"""

# 1. getting the input/creating grid
n, m = [int(i) for i in input().split()]
grid = []
for _ in range(n):
    grid.append(list(input()))

# 2. creating essential variables
directions = ((1,0), (0,1), (-1,0), (0,-1))
visited = [[-1 for _ in range(m)] for _ in range(n)]
camera = [[False for _ in range(m)] for _ in range(n)]
conveyors = ("L", "R", "U", "D")

# 3. initialize the visited grid
for i in range(n):
    for j in range(m):
        if grid[i][j] == ".":
            visited[i][j] = 0
        elif grid[i][j] in conveyors:
            visited[i][j] = -2
        elif grid[i][j] == "S":
            start = (i, j, 0)
# keep in mind that this only considers the (.) cells - turns them into 0
# everything else is marked as -1

# 4. initialize the camera grid

# simple function that checks if a point is in the bounds of the grid size
def inBounds(x, y):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    return True

# 4 cases:
# 1. (.) - toggle camera cell
# 2. wall - break
# 3. conveyor - don't count but continue
# 4. another camera - break? / or continue?
# note that conveyors and cameras are -1 on the visited grid (treated as walls)
spawnkill = False
for i in range(n):
    for j in range(m):
        if grid[i][j] == "C":
            for d in directions:
                temp_x, temp_y = i, j
                while inBounds(temp_x, temp_y):
                    temp_camera = grid[temp_x][temp_y]
                    if temp_camera == ".":
                        camera[temp_x][temp_y] = True
                    elif temp_camera == "W": 
                        break
                    elif temp_camera == "S":
                        spawnkill = True
                    elif temp_camera == "C":
                        pass # pass for now
                    temp_x += d[0]
                    temp_y += d[1]



# 5. create functions for the validMove and conveyorMove

# validMove is only used for normal traversal (not a conveyor)
# 7 cases
# 1. (.) - proceed - add to queue
# 2. visited node > 0 - traversed before visited - do not proceed
# 3. wall - -1 on the visited grid
# 4. conveyor - -2 on the visited grid
# 5. camera/camera watched - marked True on the camera grid
# 6. start - -1 on the visited grid
# 7. out of bounds - do not proceed
def validMove(x, y):
    if x < 0 or y < 0 or x >= n or y >= m: # out of bounds error prevention
        return False
    if visited[x][y] > 0: # visited (.) node
        return False
    if visited[x][y] == -1:
        return False
    if camera[x][y]:
        return False
    return True

# use when the next node is a conveyor node
def conveyorMove(x, y):
    if x < 0 or y < 0 or x >= n or y >= m: # out of bounds error prevention
        return False
    if visited[x][y] == -2:
        visited[x][y] = -1
        if grid[x][y] == "L":
            return conveyorMove(x, y-1)
        if grid[x][y] == "R":
            return conveyorMove(x, y+1)
        if grid[x][y] == "U":
            return conveyorMove(x-1, y)
        if grid[x][y] == "D":
            return conveyorMove(x+1, y)
    if validMove(x, y):
        return [x, y, 1]
    return False


# 6. attempt the BFS algorithm using the functions above

if spawnkill:
    queue = []
else:
    queue = [start]
while queue:
    # get data from the queue pop
    curr = queue.pop(0)
    curr_x, curr_y = curr[0], curr[1]
    curr_distance = curr[2]

    for d in directions:
        next_x = curr_x+d[0]
        next_y = curr_y+d[1]
        if inBounds(next_x, next_y):
            if grid[next_x][next_y] in conveyors:
                temp_conveyor = conveyorMove(next_x, next_y)
                if temp_conveyor != False:
                    visited[temp_conveyor[0]][temp_conveyor[1]] = curr_distance+temp_conveyor[2]
                    queue.append((temp_conveyor[0], temp_conveyor[1], curr_distance+temp_conveyor[2]))
            else: # not in conveyors
                if validMove(next_x, next_y):
                    queue.append((next_x, next_y, curr_distance+1))
                    visited[next_x][next_y] = curr_distance+1


# print("-=BEFORE=-")
# for i in grid:
#     print(i)
# for i in visited:
#     print(i)
# for i in camera:
#     print(i)
# print()

# print("-=AFTER=-")
# for i in grid:
#     print(i)
# for i in visited:
#     print(i)

for i in visited:
    for j in i:
        if j == -2:
            continue
        elif j != -1:
            print(-1) if j == 0 else print(j)


