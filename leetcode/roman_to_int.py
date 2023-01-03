def romanToInt(str):
    hash_table = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    i = len(str) - 1
    value = 0
    a = hash_table[str[i]]
    b = hash_table[str[i-1]]
    while(i >= 0):
        if hash_table[str[i]] > hash_table[str[i-1]] and i - 1 >= 0:
            value = value + hash_table[str[i]] - hash_table[str[i-1]]
            i = i - 2
        else:
            value = value + hash_table[str[i]]
            i = i - 1

    return value


        

