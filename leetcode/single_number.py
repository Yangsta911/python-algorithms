def singleNumber(nums):
    counter_dict = {i:nums.count(i) for i in nums}
    for key, value in counter_dict.items():
        if value == 1:
            return key

nums = [2,2,1]
singleNumber(nums)