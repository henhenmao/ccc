
n = int(input())
for _ in range(n):
    s = input()
    i = 0

    total = 0
    res = ""
    while i < len(s):
        curr = s[i]

        if curr == "-":
            temp = "-"
            i += 1
            while i < len(s):
                if not s[i].isdigit():
                    i -= 1
                    break
                temp += s[i]
                i += 1
            total += int(temp)

        elif curr.isdigit():
            temp = ""
            while i < len(s):
                if not s[i].isdigit():
                    i -= 1
                    break
                temp += s[i]
                i += 1
            total += int(temp)


        
        elif curr.islower():
            i += 1
            continue
        else:
            res += curr
        i += 1

    print(res + str(total))

