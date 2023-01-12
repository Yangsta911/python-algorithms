 
def searchInsert(nums, target):    
    low = 0
    high = len(nums) - 1
    mid = 0
 
    while low <= high:
 
        mid = (high + low) // 2
 
        if nums[mid] < target:
            low = mid + 1
 
        elif nums[mid] > target:
            high = mid - 1
 
        else:
            return mid
    if target < nums[mid]:
        return mid
    else:
        return mid + 1



nums = [1,3,5,6]
target = 5
print(searchInsert(nums, target))