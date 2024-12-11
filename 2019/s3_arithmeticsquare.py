"""
get all of the inital square scenarios
- one single unit
    - fill every cell with the single unit -> arithmetic sequence
- two units in a row (a b x)
    - x = b-a -> arithmetic sequence for the given row
    - if no other rows are filled out then duplicate the first one
        a b c
        a b c
        a b c
- first row completely filled + 2 rows empty
    - just duplicate the first row twice just like above

- first row filled and one unit in the second row
    a b c
    d x x
    x x x
    - take first row (a b c) and increment everything by (d-a) then just put it all in the second row
        second row = (a+(d-a)), (b+(d-a)), (c+(d-a))
        example:
        1 2 3    1 2 3                    1 2 3
        4 x x -> 4 (2+(4-1)) (3+(4-1)) -> 4 5 6
        x x x    x x x                    x x x
    
do the same thing but for columns rotated 90 degrees or something

"""

# getting the input inital grid
# probably better to get each row as it's own variable instead of one 2d grid
# so that its easier to work with
# i'm going to jump off a building

# getting the grid input and seapartaing them into 3 rows and 3 columns
# the rows and colmsn will share values

grid = [input().split(), input().split(), input().split()]
rows = [[], [], []]
cols = [[], [], []]

def getGrid():
    for i in grid[0]:
        if i == "X":
            rows[0].append("X")
        else:
            rows[0].append(int(i))
    for i in grid[1]:
        if i == "X":
            rows[1].append("X")
        else:
            rows[1].append(int(i))
    for i in grid[2]:
        if i == "X":
            rows[2].append("X")
        else:
            rows[2].append(int(i))

    for i in range(3):
        if grid[i][0] == "X":
            cols[0].append("X")
        else:
            cols[0].append(int(grid[i][0]))
    for i in range(3):
        if grid[i][1] == "X":
            cols[1].append("X")
        else:
            cols[1].append(int(grid[i][1]))   
    for i in range(3):
        if grid[i][2] == "X":
            cols[2].append("X")
        else:
            cols[2].append(int(grid[i][2]))
def countX(nums):
    return nums.count("X")
def fillLine(line):
    xcount = line.count("X")
    if xcount == 0:
        pass
    elif xcount == 1:
        if line[2] == "X":
            line[2] = line[1]+(line[1]-line[0])
        elif line[1] == "X":
            line[1] = line[0]+((line[2]-line[0])/2)
        elif line[0] == "X":
            line[0] = line[1]-(line[2]-line[1])
    return line
def matchLines():
    for i in range(3):
        for j in range(3):
            if rows[i][j] == cols[j][i]:
                pass
            if rows[i][j] == "X":
                rows[i][j] = cols[j][i]
            elif cols[j][i] == "X":
                cols[j][i] = rows[i][j]
def betterFill(filled, unfilled):
    for i in range(3):
        if unfilled[i] != "X":
            diff = unfilled[i]-filled[i]
    for i in range(3):
        unfilled[i] = filled[i]+diff
    return unfilled
def doBetterFill():
    if countX(rows[0]) == 0 and countX(rows[1]) == 2:
        rows[1] = betterFill(rows[0], rows[1])
    elif countX(rows[2]) == 0 and countX(rows[1]) == 2:
        rows[1] = betterFill(rows[2], rows[1])
    elif countX(rows[1]) == 0:
        if countX(rows[0]) == 2:
            rows[0] = betterFill(rows[1], rows[0])
        if countX(rows[2]) == 2:
            rows[2] = betterFill(rows[1], rows[2])
    
    if countX(cols[0]) == 0 and countX(cols[1]) == 2:
        cols[1] = betterFill(cols[0], cols[1])
    elif countX(cols[2]) == 0 and countX(cols[1]) == 2:
        cols[1] = betterFill(cols[2], cols[1])
    elif countX(cols[1]) == 0:
        if countX(cols[0]) == 2:
            cols[0] = betterFill(cols[1], cols[0])
        if countX(cols[2]) == 2:
            cols[2] = betterFill(cols[1], cols[2])
def emptyGridCheck():
    totalX = countX(rows[0]) + countX(rows[1]) + countX(rows[2])
    if totalX == 9:
        rows[0] = [0, 0, 0]
        rows[1] = [0, 0, 0]
        rows[2] = [0, 0, 0]
    elif totalX == 8:
        for i in rows:
            for j in i:
                if j != "X":
                    rows[0] = [j, j, j]
                    rows[1] = [j, j, j]
                    rows[2] = [j, j, j]
def emptyCheck():
    emptyCount = 0
    fullRow = []
    for row in rows:
        if countX(row) == 0: # if row is full
            fullRow = row
        elif countX(row) == 3: # all empty
            emptyCount += 1
    if emptyCount == 2 and fullRow != []:
        rows[0] = fullRow
        rows[1] = fullRow
        rows[2] = fullRow

    emptyCount = 0
    fullCol = []
    for col in cols:
        if countX(col) == 0: # if row is full
            fullCol = col
        elif countX(col) == 3: # all empty
            emptyCount += 1
    if emptyCount == 2 and fullCol != []:
        cols[0] = fullCol
        cols[1] = fullCol
        cols[2] = fullCol
def twoCheck():
    for row in rows:
        fillLine(row)
    for col in cols:
        fillLine(col)
    matchLines()
    for row in rows:
        fillLine(row)
    for col in cols:
        fillLine(col)
def checkSequence(nums):
    return (nums[2]-nums[1]) == (nums[1]-nums[0])
def threeCheck():
    if countX(rows[0]) >= 2 and countX(rows[1]) >= 2 and countX(rows[2]) >= 2 and countX(cols[0]) >= 2 and countX(cols[1]) >= 2 and countX(cols[2]) >= 2:
        tempRow = []
        tempCol = []
        for row in range(3):
            if countX(rows[row]) == 3:
                continue
            for i in range(3):
                if rows[row][i] != "X":
                    tempRow.append(rows[row][i])
                    break
        for col in range(3):
            if countX(cols[col]) == 3:
                continue
            for i in range(3):
                if cols[col][i] != "X":
                    # rows[row] = [rows[row][i]]*3
                    tempCol.append(cols[col][i])
                    break
        if checkSequence(tempRow):
            for row in range(3):
                rows[row] = [tempRow[row]] * 3
        else:
            for col in range(3):
                cols[col] = [tempCol[col]] * 3
def sevenCheck():
    totalX = countX(rows[0]) + countX(rows[1]) + countX(rows[2])
    if totalX == 7:
        one = countX(rows[0]) == 2
        two = countX(rows[1]) == 2
        three = countX(rows[2]) == 2
        if two == False:
            for col in range(3):
                if countX(cols[col]) == 3:
                    continue
                for i in range(3):
                    if cols[col][i] != "X":
                        cols[col] = [cols[col][i]]*3
                        break
        else:
            for row in range(3):
                if countX(rows[row]) == 3:
                    continue
                for i in range(3):
                    if rows[row][i] != "X":
                        rows[row] = [rows[row][i]]*3
                        break


getGrid()

# solves a 2x2 grid
twoCheck()
matchLines()

sevenCheck()
matchLines()

emptyGridCheck()
matchLines()

emptyCheck()
matchLines()


threeCheck()
matchLines()


twoCheck()
matchLines()

# solves a grid that has no 2x2 grid but one full row and adjacent item
doBetterFill()
matchLines()

doBetterFill()
matchLines()

twoCheck()
matchLines()

# print()
# print("-=Rows=-")
# for i in rows:
#     print(i)
# print()
# print("-=Cols=-")
# for i in cols:
#     print(i)

for row in rows:
    print(" ".join([str(int(i)) for i in row]))