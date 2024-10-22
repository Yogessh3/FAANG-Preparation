#Time - O(n) || Space - O(1)
def isPalindrome(s):
    left = 0
    right = len(s) - 1
    while left <= right :
        if(isAlphaNumeric(s[left]) and isAlphaNumeric(s[right])):
            if(s[left].lower() == s[right].lower()):
                left += 1
                right -= 1
            else:
                return False
        else :
            if not isAlphaNumeric(s[left]):
                left += 1
            if not isAlphaNumeric(s[right]):
                right -= 1
    return True

def isAlphaNumeric(char):
    return True if (ord(char.lower()) >= 97 and ord(char.lower()) <= 122) or (char in "0123456789") else False 