class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        cnt = 0
        while n:
            print("Step", cnt + 1)
            print(n & 1)
            print(n >> 1)
            res += 1 if n & 1 else 0
            n >>= 1
            cnt += 1
        return res