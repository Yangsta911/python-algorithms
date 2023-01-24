import math

def plusOne(digits):
    number = 0
    multiplier = 1
    for i in reversed(digits):
        number = number + i * multiplier
        multiplier = multiplier * 10

    number = number + 1
    return_digits = [0] * len(str(number))
    length = len(str(number))
    length = length - 1
    while length >= 0:
        temp = number % 10
        number = math.floor(number / 10)
        return_digits[length] = temp
        length -= 1

    return return_digits


