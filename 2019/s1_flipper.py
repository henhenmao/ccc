


def hor():
    global nums
    nums[0][0], nums[1][0] = nums[1][0], nums[0][0]
    nums[0][1], nums[1][1] = nums[1][1], nums[0][1]

def ver():
    global nums
    nums[0][0], nums[0][1] = nums[0][1], nums[0][0]
    nums[1][0], nums[1][1] = nums[1][1], nums[1][0]


nums = [[1,2],
        [3,4]]

for c in input():
    hor() if c == "H" else ver()

print(f"{nums[0][0]} {nums[0][1]}")
print(f"{nums[1][0]} {nums[1][1]}")