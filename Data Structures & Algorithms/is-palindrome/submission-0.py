class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ''
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        
        n = len(newStr)
        for i in range(n):
            if newStr[i] != newStr[n - i - 1]:
                return False
        return True