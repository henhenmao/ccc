


"""
notes: 
- current bfs algorithm checks all nearby eight directions for each current node
    - in a word search you need you only go in a straight line
    - add a variable to deal with that
        - consider the right angle word search later after you can properly implement the striahgt line
        - remember to add both horizontla and diagonal word
"""
"""
more notes:
The first line of input will contain a string of distinct uppercase letters, W,
representing the word you are to search for in the grid. The length of W will be at least two
- since the word input (W) contains DISTINCT characters only (NO DUPLICATES)
    - YOU DO NOT NEED A VISITED DATA STRUCTURE!!!
    - YOU WILL NEVER ACCIDENTALLY REUSE RELOOP BECAUSE ALL LETTERS IN WORD ARE DISTINCT
    - ONLY NEED TO VALIDATE THE CORRECT LETTERS

"""

word = input()
r, c = int(input()), int(input())
grid = []
count = 0
directions = ((-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1))
for _ in range(r):
    grid.append(input().split())
# for i in grid:
#     print(i)
# given a point on the grid see if it is a valid move or not

# search function should input a point on the word search grid (matches with word[0] already)
# will search in all directions for the word from the given point
# using bfs?
def search(x, y):
    count = 0
    visited = [[False for _ in range(c)] for _ in range(r)]

    queue = [(x,y,1,-1, False)] # (x, y, word length, has perpendicular turned)

    def validMove(x, y):
        if x < 0 or y < 0 or x >= r or y >= c:
            return False
        # if visited[x][y]:
        #     return False
        return True
    
    # def turn():

    def getTurn(curr_d, d1, d2): # (0,1) - right, (1,0) - down, (-1, 0) - up, (1, 0) - down
        d = (d1, d2)
        # if d1 != 0 and d2 != 0: # diagonal
        #     return "diagonal"
        # if d == curr_d:
        #     return "straight"
        # else:
        #     return "turn"
        if d == curr_d:
            return "straight"

        if curr_d == (1,1): # down right
            if d == (1,-1) or d == (-1,1):
                return True
            return False
        elif curr_d == (1,-1): # down left
            if d == (-1,-1) or d == (1,1):
                return True
            return False
        elif curr_d == (-1,1): # up right
            if d == (-1,-1) or d == (1,1):
                return True
            return False
        elif curr_d == (-1,-1): # up left
            if d == (1,-1) or d == (-1, 1):
                return True
            return False
        
        elif curr_d == (0,1): # right
            if d == (1,0) or d == (-1,0):
                return True
            return False
        elif curr_d == (0,-1): #left
            if d == (1,0) or d == (-1,0):
                return True
            return False
        elif curr_d == (1,0): # down
            if d == (0,1) or d == (0,-1):
                return True
            return False
        elif curr_d == (-1,0): # up
            if d == (0,1) or d == (0,-1):
                return True
            return False
        
    while queue:
        curr = queue.pop(0)
        curr_x = curr[0]
        curr_y = curr[1]
        word_length = curr[2]
        curr_dir = curr[3]
        hasTurned = curr[4]

        if word_length >= len(word):
            count += 1
            # print(f"found last letter at {curr_x}, {curr_y}")
            continue

        for d in directions: # EVERY POSSIBLE EIGHT DIRECTIONS
            next_x = curr_x+d[0]
            next_y = curr_y+d[1]

            if validMove(next_x, next_y) and grid[next_x][next_y] == word[word_length]:
                turn = getTurn(curr_dir, d[0], d[1])
                if curr_dir == -1:
                    visited[next_x][next_y] = True
                    queue.append((next_x, next_y, word_length+1, (d[0], d[1]), hasTurned))
                elif turn == "straight": # straight line 
                    if (d[0], d[1]) != curr_dir: # not a straight line + diagonal = skip
                        continue
                    else: # is a straight diagonal line = proceed
                        visited[next_x][next_y] = True
                        queue.append((next_x, next_y, word_length+1, curr_dir, hasTurned))
                elif turn == True: # turn == "turn"  
                    if hasTurned:
                        continue
                    visited[next_x][next_y] = True
                    queue.append((next_x, next_y, word_length+1, (d[0], d[1]), True))
    return count

for i in range(r):
    for j in range(c):
        if grid[i][j] == word[0]:
            count += search(i, j)
print(count)

