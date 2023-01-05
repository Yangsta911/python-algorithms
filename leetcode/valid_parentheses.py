def isValid(s):
    stack = []
    hash_table = {')':'(', '}':'{', ']':'['}
    value = 0
    counter = 0
    for i in s:
        if (i == '(' or i == '{' or i == '['):
            stack.append(i)
            counter += 1
        else:
            if (stack[counter - 1] == hash_table[i]):
                stack.pop()
                counter -= 1

    if not stack:
        value = 1
    if value == 1:
        return True
    else:
        return False
