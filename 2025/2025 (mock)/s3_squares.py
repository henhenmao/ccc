

res = []

def recurse(nums):
    if nums == [1] * len(nums):
        return
    recurse_list = []
    for i in range(len(nums)-1, -1, -1):
        if nums[i] == 1:
            continue
        for j in range(1, nums[i]//2+1):

            temp = nums[:i] + [nums[i]-j] + [j] + nums[i+1:]
            if temp == sorted(temp, reverse=True):
                recurse_list.append(temp)
            # print(" ".join([str(i) for i in temp]))
                if temp not in res:
                    res.append(temp)
    for a in recurse_list:
        recurse(a)



n = int(input())
res.append([n])
recurse([n])

res.sort(key=lambda x : len(x))

# print(res)

for i in res:
    print(" ".join(str(j) for j in i))


