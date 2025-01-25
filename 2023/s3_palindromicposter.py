
# first subtask - max one r or c, n and m are max 2000x2000

n, m, r, c = [int(i) for i in input().split()]


if n != 2 or m != 2:
    grid = [["x" for _ in range(m)] for _ in range(n)]

    if r == 1:
        grid[0] = ["a" for _ in range(m)]

    if c == 1:
        for i in range(n):
            grid[i][0] = "a"

    for i in grid:
        print("".join(i))


# second subtask - n and m are always 2, 2x2 grid always
# r and c can be 0, 1, 2 each, only 9 different cases for subtask 2 - can literally be hardcoded

# n, m, r, c = [int(i) for i in input().split()]
else:
    if r == 0 and c == 0:
        print("ab")
        print("ba")
    elif r == 0 and c == 1:
        print("ab")
        print("cb")
    elif r == 0 and c == 2:
        print("ab")
        print("ab")

    elif r == 1 and c == 0:
        print("bb")
        print("ac")

    elif r == 1 and c == 1:
        print("aa")
        print("ab")

    elif r == 1 and c == 2:
        print("IMPOSSIBLE")

    elif r == 2 and c == 0:
        print("aa")
        print("bb")

    elif r == 2 and c == 1:
        print("IMPOSSIBLE")

    elif r == 2 and c == 2:
        print("aa")
        print("aa")


