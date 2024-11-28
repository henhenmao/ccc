
left, right, down, up = 100, 0, 100, 0
n = int(input())
for _ in range(n):
    dot = [int(i) for i in input().split(",")]
    if dot[0] < left:
        left = dot[0]
    if dot[0] > right:
        right = dot[0]
    if dot[1] < down:
        down = dot[1]
    if dot[1] > up:
        up = dot[1]
# print(left, right, down, up)
print(f"{left-1},{down-1}")
print(f"{right+1},{up+1}")            