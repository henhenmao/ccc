

friends = [-1 for _ in range(10005)]

n = int(input())
for _ in range(n):
    giver, receiver = [int(i) for i in input().split()]
    friends[giver] = receiver

while True:

    # for each set of inputs just go wherever the pointer leads you until one of the following happens
    # - cycle found

    start, end = [int(i) for i in input().split()]
    
    if start == 0 and end == 0:
        break
    
    count = -1
    curr = start
    visited = [False for _ in range(10005)]

    while True:
        visited[curr] = True
        curr = friends[curr]
        count += 1

        if visited[curr]:
            break

        if curr == end:
            break

        if friends[curr] == -1:
            break
    
    if curr == end:
        print(f"Yes {count}")
    else:
        print("No")

    


        


