

trout = int(input())
pike = int(input())
pickerel = int(input())
river = int(input())

points = 0

count = 0
for i in range(river//trout+1):
    for j in range(river//pike+1):
        for k in range(river//pickerel+1):
            points = trout*i + pike*j + pickerel*k
            if points <= river and (i > 0 or j > 0 or k > 0):
                print(f"{i} Brown Trout, {j} Northern Pike, {k} Yellow Pickerel")
                count += 1
print(f"Number of ways to catch fish: {count}")

