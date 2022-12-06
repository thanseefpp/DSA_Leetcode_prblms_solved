from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # mapping charCount to list Anagrams
        for s in strs:
            count = [0] * 26 # a...z
            for c in s:
                count[ord(c) - ord("a")] += 1
            res[tuple(count)].append(s)
        return res.values()
        
obj = Solution()
print(obj.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))