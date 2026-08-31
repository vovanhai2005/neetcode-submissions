class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n + 1):
            ans = 0
            tmp = i
            while tmp:
                if tmp & 1:
                    ans += 1
                tmp >>= 1

            res.append(ans)
        return res
