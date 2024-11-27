
# this question took way too long to solve for some reason

nums = []
for i in range(1, 50):
    nums.append(i**6)


a = int(input())
b = int(input())

count = 0
i = 0
while i < len(nums):
    if nums[i] >= a and nums[i] <= b:
        count += 1
    i += 1

# print(nums)
print(count)