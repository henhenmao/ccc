def escapeRoom():
  m, n = int(input()), int(input())
  board = [[int(i) for i in input().split()] for _ in range(m)]
  data = [[] for _ in range(1000001)]
  for i in range(len(board)):
    for j in range(len(board[i])):
      data[board[i][j]].append((i,j))
  visited = [[False for _ in range(n)]  for _ in range(m)]
  goal = (0,0)
  # print(board)
  queue = [(m-1, n-1)]
  while len(queue) > 0:
    curr = queue.pop()
    if curr == goal:
      print("yes")
      return
    num = (curr[0]+1)*(curr[1]+1)
    for i in data[num]:
      if not visited[i[0]][i[1]]:
        queue.append(i)
        visited[i[0]][i[1]] = True
  print("no")
escapeRoom()