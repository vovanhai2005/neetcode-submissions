class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        n = len(s)
        l = 0
        arrSet = set()

        for i in range(n):
            while s[i] in arrSet:
                arrSet.remove(s[l])
                l += 1
            arrSet.add(s[i])
            res = max(res , i - l + 1)
        return res


            