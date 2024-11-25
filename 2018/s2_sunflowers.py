

# first find out how the grid was rotated
# next rotate it based on the inital finding

def swap(a, b, x , y):
    global grid
    temp = grid[a][b]
    grid[a][b] = grid[x][y]
    grid[x][y] = temp

def rotate():
    global grid
    
    # mirrors the grid along the y-axis
    for i in range(len(grid)):
        for j in range(len(grid[i])//2):
            swap(i, j, i, len(grid[i])-j-1)
    
    # mirror along the negative slope diagonal
    # gives us a 90 degree counter clockwise rotation
    # mirroring the positive slope diagonal gives 90 degree clockwise rotation

    for i in range(len(grid)):
        for j in range(1+i, len(grid[i])):
            swap(i, j, j, i)
            
# checks if a grid is valid if it is sorted veritcally and horizontally
def done():
    global grid
    if grid[1][0] > grid[0][0] and grid[0][1] > grid[0][0]:
        return True
    return False

# getting inputs
n = int(input())
grid = []
for _ in range(n):
    grid.append([int(i) for i in input().split()])

# continue rotating by 90 degrees until the grid is valid 
while not done():
    rotate()

# printing thr grid at the end
for row in grid:
    print(" ".join([str(i) for i in row]))