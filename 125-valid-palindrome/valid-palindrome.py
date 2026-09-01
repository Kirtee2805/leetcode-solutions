class Solution(object):
    def isPalindrome(self, s):
        
        s = ''.join(c.lower() for c in s if c.isalnum())
        n = len(s)
        left = 0
        right = n-1
        while left < right:
            if s[left] != s[right]:
                return False

            left += 1
            right -= 1
        return True
        