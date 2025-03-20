

# im going to kill msyelf

s = input()
text = ""
c = int(input())


i = 0
currc = ""

while i < len(s):
    currn = ""
    if s[i].isdigit():
        currc = s[i-1]
        while i < len(s):
            if not s[i].isdigit():
                break
            currn += s[i]
            i += 1
        text += int(currn) * currc

        # print(f"currn {currn} --- currc {currc}")
    i += 1

# print(text)
print(text[c%len(text)])
# print((text*5)[:c+1])