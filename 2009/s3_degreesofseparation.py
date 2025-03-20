friends = [[],[6],[6],[4,5,6,15],[3,5,6],[3,4,6],[1,2,3,4,5,7],[6,8],[7,9],[8,10,12],
        [9,11],[10,12],[9,11,13],[12,14,15],[13],[3,13],[17,18],[16,18],[16,17],[],
        [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],
        [],[],[],[],[],[]]
# print(len(friends))

def degreesOfSeparation():
    while True:
        inp = input()
        if inp == "q":
            break
        a = int(input())
        if inp == "i":
            b = int(input())
            makeFriends(a, b)
        elif inp == "d":
            b = int(input())
            removeFriends(a, b)
        elif inp == "n":
            print(len(friends[a]))
        elif inp == "f":
            friendsOfFriends(a)
        elif inp == "s":
            b = int(input())
            print(findSeparation(a, b))

def makeFriends(a, b):
    if a not in friends[b] and b not in friends[a]:
        friends[a].append(b)
        friends[b].append(a)

def removeFriends(a, b):
    friends[a].remove(b)
    friends[b].remove(a)

def friendsOfFriends(a):
    all_friends = set()
    for i in friends[a]:
        for j in friends[i]:
            if j != a and j not in friends[a]:
                all_friends.add(j)
    print(len(all_friends))

def findSeparation(a, b):
    queue = [(a, 0)]
    visited = [False]*51
    visited[a] = True
    while len(queue) > 0:
        curr = queue.pop(0)
        if curr[0] == b:
            return curr[1]
        for i in friends[curr[0]]:
            if not visited[i]:
                queue.append((i, curr[1]+1))
                visited[i] = True
    return "Not connected"

degreesOfSeparation()