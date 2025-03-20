
n = int(input())
heights = [int(i) for i in input().split()]
widths = [int(i) for i in input().split()]
area = 0
for i in range(len(widths)):
    area += (heights[i]+heights[i+1])/2*widths[i]

print(area)