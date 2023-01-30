from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # adding zero to first and last index
        f = [0] + flowerbed + [0]
        
        for i in range(1,len(f)-1): #skip first and last iteration
            # array of previous value, current value, next value are zeros or not checking.
            if f[i - 1] == 0 and f[i] == 0 and f[i + 1] == 0:
                # assigning value to the current index
                f[i] = 1 
                # decrementing the value.
                n -= 1
        # here checking n <= 0 will return True/False. 
        return n <= 0
      
      
      
obj = Solution()
print(obj.canPlaceFlowers(flowerbed = [1,0,0,0,1], n = 1))