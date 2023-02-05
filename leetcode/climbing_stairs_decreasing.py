def climbStairs(n):
    if (n == 1 or n == 2):
        return n

    else:
        result = climbStairs(n-1) + climbStairs(n-2)
        return result


