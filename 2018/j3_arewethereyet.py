

distances = [int(i) for i in input().split()]
for i in range(5):
    for j in range(5):
        if i == j:
            print(0, end=" ")
        else:
            start = min(i, j)
            end = max(i, j)
            print(sum(distances[start:end]), end=" ")
    print()
        
