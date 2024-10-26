#Time - O(n) || Space - O(1)
def validPalindrome(s):
    def isPalindrome(left, right):
        while left <= right:
            if(s[left] != s[right]):
                return False
            left += 1
            right -= 1
        return True
    characterDiff = 0
    left = 0
    right = len(s) - 1
    while left <= right:
        if(s[left] != s[right]):
            characterDiff += 1
            return isPalindrome(left + 1, right) or isPalindrome(left, right - 1)
        left += 1
        right -= 1
    return True

    