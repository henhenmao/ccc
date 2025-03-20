def alphaswap(s, n):
    a = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    new_s = ""
    for c in s:
        new_ord = ord(c)+n
        if new_ord > 90:
            new_ord -= 26
        new_s += chr(new_ord)
    return new_s

def simpleEncryption():
    new_message = ""
    key = input()
    key_point = 0
    message = "".join([i for i in input() if i.isalpha()])
    for c in message:
        new_message += alphaswap(c, ord(key[key_point])-65)
        key_point += 1
        if key_point == len(key):
            key_point = 0
    print(new_message)
simpleEncryption()