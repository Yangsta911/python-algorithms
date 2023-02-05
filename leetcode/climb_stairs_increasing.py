def climbStairs(N, n = 0):
    if (n == 1 or n ==2):
        result = n
    if (n < N-3):
        result = climbStairs(N, n+1) + climbStairs(N, n+2)
        return result
    




print(climbStairs(5))