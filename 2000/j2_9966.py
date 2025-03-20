
pairs = {"1":"1", "6":"9", "9":"6", "8":"8", "0":"0"}

start = int(input())
end = int(input())
count = 0
print()

for i in range(start, end+1):
    strnum = str(i)
    validnum = True
    for j in range(len(strnum)//2+1):
        if strnum[j] not in pairs or strnum[len(strnum)-j-1] not in pairs or strnum[j] != pairs[strnum[len(strnum)-j-1]]:
            validnum = False
            break
    if validnum:
        count += 1
print(count)