

def recurse(a, b, c, d):
    if a <= -1 or b <= -1 or c <= -1 or d <= -1:
        return True # previous position was losing, current position is winning
    

    if dp[a][b][c][d] != -1:
        return dp[a][b][c][d]
    
    one = recurse(a-2, b-1, c, d-2)
    two = recurse(a-1, b-1, c-1, d-1)
    three = recurse(a, b, c-2, d-1)
    four = recurse(a, b-3, c, d)
    five = recurse(a-1, b, c, d-1)

    possible_win = False
    if not one or not two or not three or not four or not five: # current position is winning if next postion is losing
        possible_win = True
    
    dp[a][b][c][d] = possible_win
    return possible_win
    



n = int(input())
for _ in range(n):

    dp = [[[[-1 for i in range(32)] for ii in range(32)] for iii in range(32)] for iv in range(32)]

    inp = [int(i) for i in input().split()]
    a, b, c, d = inp

    res = recurse(a, b, c, d)
    if res:
        print("Patrick")
    else:
        print("Roland")