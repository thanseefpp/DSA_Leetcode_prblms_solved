class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        am = s.split(" ")
        while("" in am):
          am.remove("")
        lst = am[::-1][0]
        return len(lst)

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i, length = len(s) -1, 0
        
        while s[i] == " ":
          i -= 1
        while i>=0 and s[i] != " ":
          length += 1
          i -= 1
        return length


obj = Solution()
print(obj.lengthOfLastWord(s = "   fly me   to   the moon  "))