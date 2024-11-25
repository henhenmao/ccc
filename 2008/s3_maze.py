


def bfs(grid, rows, cols): # outputs min path
    
    def valid_move(row, col):
        if row < 0 or row >= r or col < 0 or col >= c: # out of bounds
            return False
        if visited[row][col]: # already visited
            return False
        return True
    
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    queue = [(0,0,1)] # queue stores (x, y, distance)

    cross_dir = [(-1,0),(1,0),(0,1),(0,-1)]
    ver_dir = [(-1,0), (1,0)]
    hor_dir = [(0,-1), (0,1)]

    while queue:
        curr = queue.pop(0)
        curr_x = curr[0]
        curr_y = curr[1]
        curr_distance = curr[2]
        current_road = grid[curr_x][curr_y]

        if curr_x == rows-1 and curr_y == cols-1:
            return curr_distance
        
        visited[curr_x][curr_y] = True

        if current_road == "*":
            continue
        if current_road == "+":
            curr_dir = cross_dir
        elif current_road == "|":
            curr_dir = ver_dir
        elif current_road == "-":
            curr_dir = hor_dir
        
        for dir in curr_dir:
            next_x = curr_x + dir[0]
            next_y = curr_y + dir[1]
            if valid_move(next_x, next_y) and not visited[next_x][next_y]:
                queue.append((next_x, next_y, curr_distance+1)) 
    return -1

test_cases = int(input())
for _ in range(test_cases):
    r, c = int(input()), int(input())

    grid = []
    for _ in range(r):
        grid.append(input())

    print(bfs(grid, r, c))
