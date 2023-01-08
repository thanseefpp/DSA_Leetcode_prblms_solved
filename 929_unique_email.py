from typing import List


# class Solution:
#     def numUniqueEmails(self, emails: List[str]) -> int:
#         unique = set()
#         for e in emails:
#             local, domain = e.split("@")
#             local = local.split("+")[0]
#             local = local.replace(".", "")
#             unique.add((local,domain))
#         return len(unique)

# obj= Solution()
# print(obj.numUniqueEmails(["a@leetcode.com","b@leetcode.com","c@leetcode.com"]))



class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = set()
        for e in emails:
            i , local = 0 , ""
            while e[i] not in ["@","+"]:
                if e[i] != ".":
                    local += e[i] #each characters will be added to it
                i += 1
            while e[i] != "@":
                i += 1
            domain = e[i + 1:]
            unique.add((local,domain))
        return len(unique)
    

obj= Solution()
print(obj.numUniqueEmails(["a@leetcode.com","b@leetcode.com","c@leetcode.com"]))
