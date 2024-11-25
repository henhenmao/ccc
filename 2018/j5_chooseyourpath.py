

pages = int(input())
book = [[] for _ in range(pages)]

for page in range(pages):
    paths = [int(i)-1 for i in input().split()]
    if paths != [0]:
        book[page] = paths[1:]

# print(book)

shortest_path = 2000
visited = [False for _ in range(pages)]
queue = [(0, 1)] # (current page number, distance path from page 1)
while queue:
    curr = queue.pop(0)
    curr_page = curr[0]
    curr_distance = curr[1]

    if book[curr_page] == []:
        if curr_distance < shortest_path:
            shortest_path = curr_distance

    visited[curr_page] = True
    for next_page in book[curr_page]:
        if not visited[next_page]:
            queue.append((next_page, curr_distance+1))

if set(visited) == {True}:
    print("Y")
else:
    print("N")
print(shortest_path)