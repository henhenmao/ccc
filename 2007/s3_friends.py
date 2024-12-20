friends = [-1 for _ in range(10000)]

n = int(input())
for _ in range(n):
    giver, receiver = [int(i) for i in input().split()]
    friends[giver] = receiver

# find a cycle
# start from each checkGiver and check if they are friends to anyone
# count your degree of deparation on your way through
# if they come across the checkReceiver in the path then you can just return the counted degree of separation
# if there is no friend cycle circle then the path will end and you just return "no"

def dfs2(curr, start, end, count, cyclecount):

    if curr == end:
        return "Yes " + str(count)
    
    if curr == -1 or (curr == start and cyclecount != -1):
        return "No"
    
    return dfs2(friends[curr], start, end, count, cyclecount+1)


def dfs(curr, start,  end, count):
    # print(curr)
    # set current *new* node to visited

    # reached the node you are looking for
    # can return the current count to get to that node form the beginning
    if curr == end:
        # return "Yes " + str(count)
        # uses another dfs to try to traverse from end back to start 
        # if cannot go from end to start then they are not in the same circle
        # saves the current count variable and returns that if start is found
        return dfs2(curr, curr, start, count, -1)
    
    # if you cycle or find dead end without finding end node
    if curr == -1 or (curr == start and count != -1):
        return "No"

    return dfs(friends[curr], start, end, count+1)

while True:
    checkGiver, checkReceiver = [int(i) for i in input().split()]
    if checkGiver == 0 and checkReceiver == 0:
        break
    print(dfs(checkGiver, checkGiver, checkReceiver, -1))