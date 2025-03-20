
nums=[5,1,3]
target=5


def findMin():
    low = 0
    high = len(nums)-1
    while low <= high:
        mid = (low+high)//2

        if target == nums[mid]:
            return mid

        if target < nums[mid] and target >= nums[low]:
            high = mid-1
        else:
            low = mid
    return -1
    
        

print(findMin())