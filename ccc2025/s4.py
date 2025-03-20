

mincost = 10000000000000

def dfs(n, curr, tempcost, temp, visited, path):
    global mincost
    global graph
    global tunnels

    for route in graph[curr]:
        if curr == n:
            if tempcost < mincost:
                mincost = tempcost
                # print(path)
            return

        start = curr
        end = route
        for tunnel in tunnels:
            abc = tunnel
            if tunnel[:2] == [start, end] and visited[end] == False:
                visited[end] = True
                # path.append(curr)
                # print(curr)
                dfs(n, end, (tempcost + abs(temp-tunnel[2])), tunnel[2], visited, path)
                visited[end] = False
                # path.pop()
    return


n, m = [int(i) for i in input().split()]
graph = [[] for _ in range(n)]
tunnels = []

for _ in range(m):
    tunnel = [int(i) for i in input().split()]
    a = tunnel[0]-1
    b = tunnel[1]-1
    c = tunnel[2]
    graph[a].append(b)
    graph[b].append(a)

    tunnels.append([a, b, c])
    tunnels.append([b, a, c])

visited = [False for _ in range(n)]
visited[0] = True
# print(graph)
# print(tunnels)

dfs(n-1, 0, 0, 0, visited, [])
print(mincost)
# print(graph)
