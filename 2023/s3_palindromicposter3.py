



# steps to solve palindromic psoter

"""

i am so close to ending it all

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



# solving third subtask n = 2, 2 <= m <= 2000

n, m, r, c = [int(i) for i in input().split()]
grid = [["a" for _ in range(m)] for _ in range(n)]


def fillRow(row, c):
    for i in range(len(grid[row])):
        grid[row][i] = c
def fillCol(col, c):
    for i in range(len(grid)):
        grid[i][col] = c


def palindromic():
    
    if r == 1 and c == 1:
        fillRow(0, "b")
        fillCol(0, "b")
        return grid



    # checking for the impossible case
    if r == n and c == m:
        return grid
    if r == n and m % 2 == 0 and c % 2 == 1: # c is the exception
        return "IMPOSSIBLE"
    if c == m and n % 2 == 0 and r % 2 == 1: # r is th eexpceiton
        return "IMPOSSIBLE"
    
    # impossible case is handled just finish the rest

    if r == 0:
        if c == m:
            grid[0][-1] = "b"
            grid[1][-1] = "b"
        elif c == 0:
            fillRow(1, "b")
            grid[0][-1] = "b"
            grid[1][-1] = "a"
        else:
            for i in range(m-c):
                grid[0][i+c] = "b"
                grid[1][i+c] = "c"

    elif r == 1: # c cannot equal m
        if c == 0:
            fillRow(1, "b")
            grid[1][-1] = "c"
        else:
            for i in range(m-c):
                grid[1][i+c] = "b"

    elif r == 2:
        if c == 0:
            fillRow(1, "b")
        else:
            if m % 2 == 0:
                for i in range(c//2):
                    grid[1][i] = "b"
                    grid[1][m-i-1] = "b"
            
            if c % 2 == 0:
                fillRow(1, "b")
                for i in range(c//2):
                    grid[1][i] = "a"
                    grid[1][m-i-1] = "a"
            
            else:
                fillRow(1, "b")
                grid[1][m//2] = "a"
                for i in range(c//2):
                    grid[1][m//2+i+1] = "a"
                    grid[1][m//2-i-1] = "a"
    return grid
        
        



    
res = palindromic()
if res != "IMPOSSIBLE":
    for row in res:
        print("".join(row))
else:
    print("IMPOSSIBLE")