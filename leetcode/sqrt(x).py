def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


def mySqrt(x):
    factors_arr = prime_factors(x)
    n = 1
    number = 0
    power = 1
    factor_powers = {}
    sqrt = 1
    while n < len(factors_arr):
        if factors_arr[n] == factors_arr[n-1]:
            number = factors_arr[n]
            power += 1
            factor_powers[number] = power
        else:
            number = factors_arr[n]
            power = 1
            factor_powers[number] = power

        n += 1

    for i in factor_powers:
        if factor_powers[i] % 2 == 0:
            sqrt = sqrt * i
        else:
            mySqrt(i)

    return sqrt



mySqrt(275)