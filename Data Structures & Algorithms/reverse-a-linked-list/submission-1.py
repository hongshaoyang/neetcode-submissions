# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # a ->   b -> c
        #              p      c    n
        # a <-  b  <-  c
        # 
        if head is None:
            return None
        prev = head
        curr = head.next
        prev.next = None # needed for first part to break first link 
        while curr:
            n = curr.next
            curr.next = prev 
            prev = curr      # advance ptr
            curr = n         # advance ptr

            
        return prev