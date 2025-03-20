
n, m = int(input()), int(input())

grid = []
visited = [[False for _ in range(m)] for _ in range(n)]
directions = ((0,1), (1,0), (-1, 0), (0, -1))

for _ in range(n):
    grid.append(list(input()))

def validMove(x, y):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    if grid[x][y] == "*":
        return False
    if visited[x][y]:
        return False
    return True

count = 0
a, b = int(input()), int(input())
visited[a][b] = True

queue = [(a,b)]
while queue:
    curr = queue.pop(0)
    curr_x = curr[0]
    curr_y = curr[1]
    pumpkin = grid[curr_x][curr_y]

    if pumpkin == "L":
        count += 10
    elif pumpkin == "M":
        count += 5
    elif pumpkin == "S":
        count += 1
    
    for d in directions:
        next_x = curr_x + d[0]
        next_y = curr_y + d[1]
        if validMove(next_x, next_y):
            visited[next_x][next_y] = True
            queue.append((next_x, next_y))

print(count)

