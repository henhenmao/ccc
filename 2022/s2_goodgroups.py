
xconstraints = []
yconstraints = []
groups = {}

x = int(input())
for _ in range(x):
    xconstraints.append(input().split())

y = int(input())
for _ in range(y):
    yconstraints.append(input().split())

# make a hashmap for each student and each student will have the value of the two students in their group

g = int(input())
for _ in range(g):
    group = input().split()
    groups[group[0]] = [group[1], group[2]]
    groups[group[1]] = [group[0], group[2]]
    groups[group[2]] = [group[0], group[1]]

# x group - must be in the same group
# y group - must not be in the same group

# print(groups)


count = 0
for pair in xconstraints:
    a, b = pair[0], pair[1]
    if b not in groups[a]:
        count += 1
for pair in yconstraints:
    a, b = pair[0], pair[1]
    if b in groups[a]:
        count += 1
print(count)




