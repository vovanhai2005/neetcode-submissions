class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        id = {}
        l = 0

        for i in range(len(s)):
            if s[i] in id:
                l = max(l , id[s[i]] + 1)
            id[s[i]] = i
            res = max(res , i - l + 1)
        return res


            