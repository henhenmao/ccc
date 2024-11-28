

n = int(input())
sprints = []
for _ in range(n):
    sprints.append([int(i) for i in input().split()])
sprints.sort()
max_speed = 0
# speed = distance/time
for i in range(len(sprints)-1):
    a = sprints[i] # previous time/distance
    b = sprints[i+1] # afterwards time/distance
    speed = (abs(b[1]-a[1]))/(b[0]-a[0])
    if speed > max_speed:
        max_speed = speed
print(max_speed)
    
