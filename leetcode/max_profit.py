import math
def maxProfit(prices):
    size = len(prices)
    difference_price = find_price_change(prices)
    profit = maxSubArray(difference_price)
    if profit < 0:
        profit = 0
    return profit


def find_price_change(prices):
    difference = []
    for i in range (1,len(prices)):
        difference.append(prices[i] - prices[i-1])

    return difference

def maxSubArray(nums):
      dp = [0 for i in range(len(nums))]
      dp[0] = nums[0]
      for i in range(1,len(nums)):
         dp[i] = max(dp[i-1]+nums[i],nums[i])
      return max(dp)
