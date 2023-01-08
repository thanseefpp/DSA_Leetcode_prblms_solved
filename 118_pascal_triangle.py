from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        data = [[1]]
        for i in range(numRows - 1):
            temp = [0] + data[-1] + [0]
            # print('temp :',temp)
            row = []
            for j in range(len(data)+1):
                row.append(temp[j] + temp[j+1])
            data.append(row)
        return data
    
# class Solution:
#     def generate(self, numRows: int) -> List[List[int]]:
#         triangle = [[1]]
#         for i in range(1, numRows):
#             row = [0] + triangle[-1] + [0]
#             triangle.append([row[j]+row[j+1] for j in range(i+1)])
#         return triangle

obj = Solution()
print(obj.generate(5))