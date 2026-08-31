class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = {}

        for num in nums:
            cnt[num] = 1 + cnt.get(num, 0)

        arr = []
        for num, cnt in cnt.items():
            arr.append([cnt, num])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res
                
