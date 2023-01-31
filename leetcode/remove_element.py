def removeElement(nums, val):
    counter = 0
    new_nums = []
    for i in nums:
        if i != val:
            counter += 1
            new_nums.append(i)
    nums = new_nums
    return nums


 
nums = [0,1,2,2,3,0,4,2]
removeElement(nums, 2)