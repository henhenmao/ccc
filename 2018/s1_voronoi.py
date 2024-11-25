

v = int(input())
villages = []
for _ in range(v):
    villages.append(int(input()))
villages.sort()


halves = []
for i in range(len(villages)-1):
    halves.append((villages[i+1] - villages[i])/2)

# print(villages)
# print(halves)


smallest_neighborhood = 10000000001
for i in range(1, len(villages)-1):
    temp = halves[i-1] + halves[i]
    if temp < smallest_neighborhood:
        smallest_neighborhood = temp

print(round(smallest_neighborhood, 1))


