class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        n = len(s)
        
        for i in range(n):
            max_freq = 0
            count = {}
            for j in range(i , n):
                count[s[j]] = 1 + count.get(s[j] , 0)
                max_freq = max(max_freq, count[s[j]])
                if (j - i + 1) - max_freq <= k:
                    res = max(res , j - i + 1)

        return res  


