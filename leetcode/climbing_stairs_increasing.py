def climbStairs(n):
    if (n == 1 or n == 2):
        return n
    n_1 = 1
    n_2 = 2
    counter = 2
    while(counter < n):
        result = n_1 + n_2
        n_1 = n_2
        n_2 = result
        counter += 1
    return result


