class Solution:
    def longestPalindrome(self, s: str) -> str:
        resId, resLen = 0, 0
        n = len(s)
        
        for i in range(n):
            l, r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            l += 1
            r -= 1
            if r - l + 1 > resLen:
                resLen = r - l + 1
                resId = l
            l, r = i, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            l += 1
            r -= 1
            if r - l + 1 > resLen:
                resLen = r - l + 1
                resId = l
        
        return s[resId : resId + resLen]
        

