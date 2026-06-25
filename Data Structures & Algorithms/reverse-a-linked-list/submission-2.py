# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
          <-a   b-> c
            h
        p   c   

            a <-b <-c
        '''
        if not head:
            return None
        if head.next is None:
            return head
        
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev

            # update pointers
            prev = curr
            curr = nxt
        return prev
        








        