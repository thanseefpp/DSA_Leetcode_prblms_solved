from typing import List

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        rightmax = -1

        for i in range(len(arr) -1, -1 , -1):
            newValue = max(rightmax,arr[i])
            arr[i] = rightmax
            rightmax = newValue
        return arr
      
      
cl = Solution()
print(cl.replaceElements([17,18,5,4,6,1]))
