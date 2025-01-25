

n, m, r, c = [int(i) for i in input().split()]

grid = [["x" for _ in range(m)] for _ in range(n)]

for row in range(r):
    grid[row] = ["a" for _ in range(m)]

for col in range(c):
    for row in range(n):
        grid[row][col] = "a"

for i in grid:
    print("".join(i))
