import math
def mySqrt(x):
    result = 1
    for i in range (30):
        temp = result
        result = temp-(temp**2-x)/(2*temp)

    return math.floor(result)
        


        



print(mySqrt(3186225))