
# dictionary made to connect each letter to the keypad value
nums = {"a": [2, 1], 
        "b": [2, 2], 
        "c": [2, 3], 
        "d": [3, 1], 
        "e": [3, 2], 
        "f": [3, 3], 
        "g": [4, 1], 
        "h": [4, 2], 
        "i": [4, 3], 
        "j": [5, 1], 
        "k": [5, 2], 
        "l": [5, 3], 
        "m": [6, 1], 
        "n": [6, 2], 
        "o": [6, 3], 
        "p": [7, 1], 
        "q": [7, 2], 
        "r": [7, 3], 
        "s": [7, 4], 
        "t": [8, 1], 
        "u": [8, 2], 
        "v": [8, 3], 
        "w": [9, 1], 
        "x": [9, 2], 
        "y": [9, 3], 
        "z": [9, 4]}


while True:
    word = input()
    if word == "halt":
        break
    prev = -1
    count = 0
    for c in word:
        # 2 seocnd pause if two consecutive buttons
        if nums[c][0] == prev:
            count += 2
        count += nums[c][1]
        prev = nums[c][0]

    print(count)


