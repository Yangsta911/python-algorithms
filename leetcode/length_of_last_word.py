def lengthOfLastWord(s):
    counter = 0
    for i in range (len(s)-1,-1,-1):  
        if s[i] == " " and counter != 0:
            break
        elif s[i] != " ":
            counter += 1

    return counter


s = "   fly me   to   the moon  "
lengthOfLastWord(s)