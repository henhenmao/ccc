def isaword(s, b, n, m):
    if len(s) == 0:
        if b > 0 or n:
            return False
        return True
    if s[0] == "B":
        if isaword(s[1:], b+1, n, m):
            return True
        return False
    if s[0] == "A":
        if n:
            if isaword(s[1:], b, False, True):
                return True
        return False
    if s[0] == "N":
        if m:
            if isaword(s[1:], b, True, False):
                return True
        return False
    if s[0] == "S":
        if b > 0 and m:
            if isaword(s[1:], b-1, False, True):
                return True
        return False

def bananas():
    while True:
        word = input()
        if word == "X":
            break
        # print(isaword(word))
        if word == "B" or word == "BS" or word == "":
            print("NO")
        else:
            if isaword(word, 0, True, False):
                print("YES")
            else:
                print("NO")
bananas()