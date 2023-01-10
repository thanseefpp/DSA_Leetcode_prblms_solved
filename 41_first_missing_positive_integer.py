from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0
        for j in range(len(nums)):
            val = abs(nums[j]) #changing to positive integer if it's in negative value
            if 1 <= val <= len(nums):
                if nums[val - 1] > 0:
                    nums[val - 1] *= -1
                elif nums[val - 1] == 0:
                    nums[val - 1] = -1 * (len(nums) + 1)
        for k in range(1, len(nums)+ 1):
            if nums[k - 1] >= 0:
              return k
        return len(nums) + 1


obj = Solution()
print(obj.firstMissingPositive(nums=[1, 2, 0]))