def modernart():
  count = 0
  m, n = int(input()), int(input())
  rlist = [False for _ in range(m)]
  clist = [False for _ in range(n)]
  for _ in range(int(input())):
    inp = input()
    index = int(inp[2:len(inp)])-1
    if inp[0] == "R":
      rlist[index] = not rlist[index]
    else:
      clist[index] = not clist[index]
  for row in range(m):
    for col in range(n):
      if rlist[row] ^ clist[col]:
        count += 1
  print(count)
# ^ ==> True ^ True ==> False
# ^ ==> False ^ False ==> False
# ^ ==> True ^ False ==> True
modernart()