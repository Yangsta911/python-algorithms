def mySqrt(x):
    for i in range(x):
        if (i * i == x):
            return i
        elif (i * i > x):
            return i-1



print(mySqrt(275))