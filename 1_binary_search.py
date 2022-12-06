
from time import time
from typing import List

# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.

# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        print(nums)
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            else:
                if len(nums)-1 == i:
                    return -1


cls = Solution()
print(cls.search(nums = [-1,0,3,5,9,12], target = 9))
