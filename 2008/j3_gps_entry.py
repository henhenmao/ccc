


def find(c):
    for i in range(len(keyboard)):
        for j in range(len(keyboard[i])):
            if keyboard[i][j] == c:
                return [i, j]
    return "not found somehow"

def getDifference(x1, y1, x2, y2):
    return abs(x1-x2) + abs(y1-y2)


keyboard = [["A", "B", "C", "D", "E", "F"], # 5 x 6 keyboard
            ["G", "H", "I", "J", "K", "L"],
            ["M", "N", "O", "P", "Q", "R"],
            ["S", "T", "U", "V", "W", "X"],
            ["Y", "Z", " ", "-", ".", "!"]]

s = input() + "!"
s_count = 0


# starting at "A"
curr_i = 0
curr_j = 0

cursor = 0

while (s_count < len(s)):
    next_i, next_j = find(s[s_count])
    cursor += getDifference(curr_i, curr_j, next_i, next_j)
    curr_i = next_i
    curr_j = next_j
    s_count += 1
    # print(str(next_i) + " " + str(next_j))

print(cursor)


