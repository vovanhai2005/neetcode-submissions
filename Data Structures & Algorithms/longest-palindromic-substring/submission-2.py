class Solution:
    def isPalindrome(self, s: str) -> str:
        return s == s[::-1]
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0
        n = len(s)
        for i in range(n):
            for j in range(i , n):
                tmp = s[i : j + 1]
                if self.isPalindrome(tmp):
                    if len(tmp) > resLen:
                        res = tmp
                        resLen = len(tmp)
        return res