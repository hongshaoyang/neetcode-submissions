# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # init
        result = ListNode()

        # init iterators
        curr = result
        l1 = list1
        l2 = list2

        # traverse list1 and list2 while there are still values
        while (l1 is not None or l2 is not None):
            # add new node
            curr.next = ListNode()
            curr = curr.next
            if l1 is None:
                curr.val = l2.val
                l2 = l2.next
                continue
            if l2 is None:
                curr.val = l1.val
                l1 = l1.next
                continue
            
            # compare
            if l1.val < l2.val:
                curr.val = l1.val
                l1 = l1.next
            else:
                curr.val = l2.val
                l2 = l2.next        
        return result.next # return the first one

