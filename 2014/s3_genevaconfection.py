

def yum():
    n = int(input())
    stack = [] # first in last out (like pancakes!)
    candy = []
    curr = 1
    for _ in range(n):
        candy.append(int(input()))

    while candy:
        if candy[-1] == curr:
            curr += 1
            candy.pop()
        elif stack:
            if stack[-1] == curr:
                curr += 1
                stack.pop()
            else:
                stack.append(candy.pop())
        else:
            stack.append(candy.pop())
        if curr == n+1:
            return True
    
    for i in range(len(stack)-1, -1, -1):
        if stack[i] == curr:
            curr += 1
            if curr == n+1:
                return True
        else:
            return False
    return False


t = int(input())
for _ in range(t):
    print("Y") if yum() else print("N")