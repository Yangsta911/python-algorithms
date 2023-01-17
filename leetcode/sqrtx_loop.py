def mySqrt(x):
    if (x == 1 or x == 0):
        return x

    a = x//2
    for i in range(a + 1):
        if (i * i == x):
            return i
        elif (i * i > x):
            return i-1



print(mySqrt(4))