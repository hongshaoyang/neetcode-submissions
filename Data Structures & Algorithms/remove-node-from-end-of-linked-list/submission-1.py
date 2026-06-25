# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # count size of list
        curr, sz = head, 0
        while curr:
            curr = curr.next
            sz += 1

        if sz <= 1:
            return None
        
        prev, curr = None, head
        for i in range(sz - n):
            prev = curr
            curr = curr.next
        
        '''
          ->1 ->2
        p   c
        '''

        if prev:
            prev.next = curr.next
            return head
        else:
            return curr.next

        
        