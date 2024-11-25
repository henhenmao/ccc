

n = int(input())
for _ in range(n):

    s = input()

    # separating the text into substring chunks

    # adds a space between each substring chunk
    # input guaranteed to NOT have any spaces " "
    newstr = ""
    for i in range(len(s)-1):
        newstr += s[i]
        if s[i+1] != s[i]:
            newstr += " "
    newstr += s[-1]

    strlist = newstr.split() # splits by space characters
    
    # prints
    for i in range(len(strlist)):
        if i == len(strlist)-1:
            print(f"{len(strlist[i])} {strlist[i][0]}")
        else:
            print(f"{len(strlist[i])} {strlist[i][0]}", end=" ")

