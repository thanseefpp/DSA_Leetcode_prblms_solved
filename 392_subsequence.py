# class Solution:
#     def isSubsequence(self, s: str, t: str) -> bool:
#         if s == "":
#             return True
#         else:
#             br = ""
#             ln = 0
#             for i in range(len(t)):
#                 if t[i] == s[ln]:
#                     br += t[i]
#                     ln += 1
#                     if s == br:
#                         break
#                     else:
#                         pass
#             return s == br

# class Solution:
#     def isSubsequence(self, s: str, t: str) -> bool:
#         br = ""
#         for i in s:
#             print('i',i)
#             for k in t:
#                 # print('k',k)
#                 if i == k:
#                     br += k
#                     print('br',br)
#         return s == br
# class Solution:
#     def isSubsequence(self, s: str, t: str) -> bool:
#         I = -1
#         for i in s:
#             I = t.find(i, I+1)
#             if I == -1:
#                 return False
#         return True

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i,j = 0,0
        while i < len(s) and j< len(t):
            if s[i] == t[j]:
                i += 1
            j+=1
        return True if i == len(s) else False
  
obj = Solution()
# print(obj.isSubsequence(s = "ab", t = "baab"))
# print(obj.isSubsequence(s="b", t="abc"))
print(obj.isSubsequence(s="abc", t="ahbgdc"))
