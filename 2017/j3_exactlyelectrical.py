
start = [int(i) for i in input().split()]
end = [int(i) for i in input().split()]
battery = int(input())

x_diff = abs(start[0] - end[0])
y_diff = abs(start[1] - end[1])

print("Y") if ((x_diff+y_diff)%2 == battery%2) and (battery >= x_diff+y_diff) else print("N")