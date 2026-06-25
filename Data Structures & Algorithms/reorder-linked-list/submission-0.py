# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        '''
            2 -> 4 ->6 ->8
        p   f    n       l


            2 ->8 ->4 ->6
        '''
        fast, slow = head, head
        while fast:
            if not fast.next:
                break
            slow = slow.next
            fast = fast.next.next
        
        # slow is at start of second list
        # reverse LL starting at slow

        prev = None
        curr = slow.next
        slow.next = None # break original LL into 2 

        '''
           <-1 <-2 ->3
            p   l2  n
            1 <-2 <-3
        '''
        while curr:
            n = curr.next
            curr.next = prev

            # update pointers
            prev = curr
            curr = n
        
        # prev is end of LL
        # merge 2 lists starting with head, prev
        '''
        a ->c ->e
        l1  n1
        b ->d ->f
        l2  n2


        a   c ->e
        v -^
        b ->d ->f
        '''
        l1, l2 = head, prev
        while True:
            if not l2:
                break
            n1, n2 = l1.next, l2.next

            l1.next = l2
            l2.next = n1

            # update pointers
            l1, l2 = n1, n2



