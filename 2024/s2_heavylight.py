


def aaaa(s):
    a = {}
    for c in s:
        if c in a:
            a[c] += 1
        else:
            a[c] = 1

    comp = False
    if a[s[0]] > 1:
        comp = True
    else:
        comp = False
    for i in range(1, len(s)):
        if comp: # heavy
            if a[s[i]] <= 1:
                comp = False
            else:
                return False
        else: # lgiht
            if a[s[i]] > 1:
                comp = True
            else:
                return False
    return True


t, n = [int(i) for i in input().split()]
for _ in range(t):
    s = input()
    print("T") if aaaa(s) else print("F")

