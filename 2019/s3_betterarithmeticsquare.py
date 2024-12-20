
# rewrite arithmetic square from scratch
# 1536

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
def countVariables(r, c):
    countr = 0
    countc = 0
    oddeven = "even"

    for i in range(3): # counting within the row
        if i == c:
            continue
        if rows[r][i] == "X":
            countr += 1
    for i in range(3):
        if i == r:
            continue
        if rows[i][c] == "X":
            countc += 1

    if r == 0 and rows[2][c] != "X":
        if rows[2][c] % 2 == 0: # even
            oddeven = "even"
        else:
            oddeven = "odd"
    elif r == 2 and rows[0][c] != "X":
        if rows[0][c] % 2 == 0:
            oddeven = "even"
        else:
            oddeven = "odd"
    if c == 0 and rows[r][2] != "X":
        if rows[r][2] % 2 == 0:
            oddeven = "even"
        else:
            oddeven = "odd"
    elif c == 2 and rows[r][0] != "X":
        if rows[r][0] % 2 == 0:
            oddeven = "even"
        else:
            oddeven = "odd"

    if countr >= 2 or countc >= 2:
        return (True, oddeven)
    return (False, oddeven)
def fillLine(line):
    xcount = line.count("X")
    if xcount == 1:
        # print("two check was performed")
        if line[2] == "X":
            # line[2] = line[1]+(line[1]-line[0])
            line[2] = int(2*line[1]-line[0])
        elif line[1] == "X":
            # line[1] = line[0]+((line[2]-line[0])/2)
            line[1] = int((line[0] + line[2])/2)
        elif line[0] == "X":
            # line[0] = line[1]-(line[2]-line[1])
            line[0] = int(2*line[1]-line[2])
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
            # if rows[i][j] != "X" and cols[j][i] != "X" and rows[i][j] != cols[j][i]:
                # print("semthing is very veyr worng")
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
    matchLines()
def fillFree():
    for i in range(3):
        for j in range(3):
            temp = countVariables(i, j)
            if rows[i][j] == "X" and temp[0]:
                if temp[1] == "even":
                    rows[i][j] = 0
                else:
                    rows[i][j] = 1
                matchLines()
            twoCheck()
    matchLines()
def emptyGridCheck():
    totalX = countX(rows[0]) + countX(rows[1]) + countX(rows[2])
    if totalX == 9:
        # print("emptygridcheck was performed")
        rows[0] = [0, 0, 0]
        rows[1] = [0, 0, 0]
        rows[2] = [0, 0, 0]
    elif totalX == 8:
        # print("one element found in empty grid")
        for i in rows:
            for j in i:
                if j != "X":
                    rows[0] = [j, j, j]
                    rows[1] = [j, j, j]
                    rows[2] = [j, j, j]
    matchLines()
def betterFill(filled, unfilled):
    # print("betterfill was perfoemed")
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
            matchLines()
        if countX(rows[2]) == 2:
            rows[2] = betterFill(rows[1], rows[2])
            matchLines()
    if countX(cols[0]) == 0 and countX(cols[1]) == 2:
        cols[1] = betterFill(cols[0], cols[1])
    elif countX(cols[2]) == 0 and countX(cols[1]) == 2:
        cols[1] = betterFill(cols[2], cols[1])
    elif countX(cols[1]) == 0:
        if countX(cols[0]) == 2:
            cols[0] = betterFill(cols[1], cols[0])
            matchLines()
        if countX(cols[2]) == 2:
            cols[2] = betterFill(cols[1], cols[2])
            matchLines()
    matchLines()
def threeCheck():
    paths = ((0, 1), (1, 0), (1, 2), (2, 1))
    if countX(rows[0]) >= 2 and countX(rows[1]) >= 2 and countX(rows[2]) >= 2 and countX(cols[0]) >= 2 and countX(cols[1]) >= 2 and countX(cols[2]) >= 2:
        if (rows[0][0] != "X" and rows[2][2] != "X") or (rows[2][0] != "X" and rows[0][2] != "X"):
            rows[1][0] = rows[1][1]
        else:
            for path in paths:
                if rows[path[0]][path[1]] != "X":
                    rows[1][1] = rows[path[0]][path[1]]
                    break
    matchLines()
def gridX():
    total = 0
    for row in rows:
        total += countX(row)
    return total

getGrid()

emptyGridCheck()

while gridX() != 0:
    twoCheck()
    threeCheck()
    twoCheck()
    for _ in range(99):
        fillFree()
        twoCheck()
    doBetterFill()
    twoCheck()

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