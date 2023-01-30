# import re
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         valid_string = re.sub(r'[^\w]', '', s.lower()) 
#         all_words = [letter for letter in valid_string if letter not in "_"]
#         return "".join(all_words) == "".join(all_words[::-1])
        
        
# obj = Solution()
# # obj.isPalindrome(s = "A man, a plan, a canal: Panama")

# # testcase
# print(obj.isPalindrome(s = "ab_a"))
# s = "A man, a plan, a canal: Panama"

# Solution 2
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l,r = 0, len(s) - 1
        
        while l < r:
            # print(s[l],s[r])
            while l < r and not self.isAlphaNum(s[l]):
                l += 1
            while r > l and not self.isAlphaNum(s[r]):
                r -= 1
            print(s[l],s[r])
            if s[l].lower() != s[r].lower():
                return False
            l,r = l + 1, r - 1
        return True
    
    def isAlphaNum(self,letter):
        return (ord('A') <= ord(letter) <= ord('Z') or
                ord('a') <= ord(letter) <= ord('z') or 
                ord('0') <= ord(letter) <= ord('9'))
        
obj = Solution()
print(obj.isPalindrome(s = "A man, a plan, a canal: Panama"))

# testcase
# print(obj.isPalindrome(s = "ab_a"))