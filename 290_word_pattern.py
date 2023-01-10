class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        splitted_data = s.split(' ')
        for i in pattern:
            print(splitted_data)
        return True
          
          
obj = Solution()
print(obj.wordPattern(pattern = "abba", s="dog cat cat dog"))