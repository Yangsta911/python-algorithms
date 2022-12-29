
def twoSum(nums, target):
    result_one = 0
    for i in nums:
        result_two = 0
        for j in nums:
            if result_two == 0:
                result_two += 1                
            elif i + j == target:
                array = [result_one,result_two]
                return array
            else:
                result_two += 1
        result_one += 1
    array = []
    return array

