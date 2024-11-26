
# unfinished beacuse i'm not smart enoughf ro the question yet

graph = {1:[4, 7], 2:[1], 3:[4, 5], 4:[], 5:[], 6:[], 7:[]}

graph2 = [[], # useless 0 index
          [4, 7],
          [1],
          [4,5],
          [],
          [],
          [],
          []]

while True:
    a = int(input())
    b = int(input())
    if a == 0 or b == 0:
        print("input has stopped")
        break
    graph[a].append(b)
    graph2[a].append(b)



state = [0] * 7
def dfs(node):
    if state[node] == 1: # in recursion stack
        return True
    if state[node] == 2: # already visited node
        return False
    state[node] == 1 # put in recuresion stack
    for n in graph[node]:
        dfs(n)
    state[node] = 2 # set as visited