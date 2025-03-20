

cross_dir = [(-1,0),(1,0),(0,1),(0,-1)]
ver_dir = [(-1,0), (1,0)]
hor_dir = [(0,-1), (0,1)]

def bfs(grid, rows, cols):
    
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    visited[0][0] = True
    queue = [(0,0,1)] # (x, y, distance) for each node

    def validMove(x, y):
        if x < 0 or x >= r or y < 0 or y >= c:
            return False
        if visited[x][y]:
            return False
        if grid[x][y] == "*":
            return False
        return True
    
    while queue:
        curr = queue.pop(0)
        curr_x = curr[0]
        curr_y = curr[1]
        curr_distance = curr[2]
        curr_road = grid[curr_x][curr_y]

        if curr_x == rows-1 and curr_y == cols-1:
            return curr_distance

        if curr_road == "*":
            continue
        elif curr_road == "+":
            curr_dir = cross_dir
        elif curr_road == "|":
            curr_dir = ver_dir
        elif curr_road == "-":
            curr_dir = hor_dir
        
        for d in curr_dir:
            next_x = curr_x+d[0]
            next_y = curr_y+d[1]
            if validMove(next_x, next_y):
                visited[next_x][next_y] = True
                queue.append((next_x, next_y, curr_distance+1))
    return -1
                

test_cases = int(input())
for _ in range(test_cases):
    r, c = int(input()), int(input())
    grid = []
    for _ in range(r):
        grid.append(list(input()))
    
    print(bfs(grid, r, c))