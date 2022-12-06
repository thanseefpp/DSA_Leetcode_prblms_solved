from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)
        
obj = Solution()
nums = [1,2,3,1]
print(obj.containsDuplicate(nums))