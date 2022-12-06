from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0,len(nums)-1):
            print("i",i)
            for j in range(1,len(nums)):
                print("j",j)
                if nums[i] + nums[j] == target:
                    return [i,j]
                
        return [0]


cls = Solution()
print(cls.twoSum(nums = [3,2,4], target = 6))




# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         res = {}
#         for i, j in enumerate(nums):
#             if j not in res:
#                 res[target - j] = i
#                 continue
#             return [i, res[j]]