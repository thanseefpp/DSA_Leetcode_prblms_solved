from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        # print(len(strs[0]))
        for i in range(len(strs[0])):
            for s in strs:
                # print(len(s))
                if i == len(s) or s[i] != strs[0][i]:
                    # print("this",i,s[i],strs[0][i])
                    return res
            res += strs[0][i]       
        return res
      
obj = Solution()
print(obj.longestCommonPrefix(["flower","flow","flight"]))