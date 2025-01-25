

from itertools import groupby

def convert(n):
    res = ""
    groups = [list(i) for _, i in groupby(str(n))]
    for group in groups:
        res += f"{len(group)}{group[0]}"
    return res


n = int(input())
s = input()

for _ in range(n):
    s = convert(s)
print(s)

    