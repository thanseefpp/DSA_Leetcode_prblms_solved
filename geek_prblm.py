# User function template for Python

import math


class Solution:
    # Function to reverse every sub-array group of size k.
    def reverseInGroups(self, arr, N, K):
        ar = arr[0:K]
        br = arr[K:]
        a = ar[::-1]
        b = br[::-1]
        return a+b


# {
 # Driver Code Starts
# Initial template for Python

ob = Solution()
arr = [1,2,3,4,5]
N   = 5
K = 3
print(ob.reverseInGroups(arr, N, K))

# def main():
#     T = int(input())
#     while(T > 0):
#         nk = [int(x) for x in input().strip().split()]
#         N = nk[0]
#         K = nk[1]
#         arr = [int(x) for x in input().strip().split()]

#         ob = Solution()
#         ob.reverseInGroups(arr, N, K)
#         for i in arr:
#             print(i, end=" ")
#         print()
#         T -= 1


# if __name__ == "__main__":
#     main()


# } Driver Code Ends
