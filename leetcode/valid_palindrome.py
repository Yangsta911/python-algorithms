def isPalindrome(s):
    new_s = ''.join(filter(str.isalnum, s))
    new_s = new_s.lower()
    counter = 0
    mid = len(new_s) // 2
    for i in range (mid):
      if (new_s[i] == new_s[len(new_s)-1-i]):
          counter += 1
    if counter == mid:
       return True
    else:
       return False
    

s = ':<:">{}(?)/@!#$%'
print(isPalindrome(s))
