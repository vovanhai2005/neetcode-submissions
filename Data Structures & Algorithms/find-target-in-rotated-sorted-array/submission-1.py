class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        
        def binary_search(l: int, r:int, target:int) -> int:
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            return -1
        
        res = binary_search(0, l - 1, target)
        if res != -1:
            return res
        res = binary_search(l, len(nums) - 1, target)
        return res


        
