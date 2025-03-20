

n, m, r, c = [int(i) for i in input().split()]

grid = [["x" for _ in range(m)] for _ in range(n)]

for row in range(r):
    grid[row] = ["a" for _ in range(m)]

for col in range(c):
    for row in range(n):
        grid[row][col] = "a"

for i in grid:
    print("".join(i))





# steps to solve palindromic psoter

"""

subtask 3
- checking for impossible case:
    - if either R or C are equal to the corresponding full size (R == N or C == M):
        - and the exception's full size is an even number (ex. R == N, M % 2 = 0)
            - and the exception itself is an odd number (R == N, M % 2 = 0, C % 2 = 1)
                - return as impossible
- R = 0 and C = 0:
    for the first row, fill with a's, but make last column b
    for the second row, fill with b's but make the last column a
- R = 0 and M > C > 0:
    fill in the first C columns with a's
    make remaining columns bc's
- R = 1 and M > C:
    fill in the first row with a's
    - C = 0:
        fill second row with b's, but make last column c
    - C > 0:
        for the second row, fill first C cells with a's, fill remaining with b's
- R = 2 and C < M:
    fill in the first row with a's
    fill in the second row with a's
    - M is even (C must be odd):
        replace the ends of the second row C/2 times with b's
    - M is odd 
        - C is odd
            replace from the middle with b's
        - C is even 
            replace the ends of the second row with b's
- C = M (R is not 1)
    - R is 0
        fill all columns with aa's and replace the last column with bb
    - R is 2 (R == N and C == M)
        fill everything with a
"""