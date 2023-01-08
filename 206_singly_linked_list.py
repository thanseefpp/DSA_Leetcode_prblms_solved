# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev,curr = None,head
        # T O(n)  Memory O(1) because we are using pointers.
        while curr:
          next = curr.next
          curr.next = prev
          prev = curr
          curr = next
        return prev

obj = Solution()
print(obj.reverseList(head=[1, 2, 3, 4, 5]))
