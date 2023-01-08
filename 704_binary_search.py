from typing import List

# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         i = 0
#         while i < len(nums):
#             if nums[i] == target:
#                 return i
#             i += 1
#         return -1


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            m = r + l // 2
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        return -1


obj = Solution()
print(obj.search(nums=[5], target=5))
