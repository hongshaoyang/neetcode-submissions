# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     # 
    #     while True:

    #         n = head.next
    #         if n is None:
    #             break
    #         n.next = head
    #         head = n
    #     return head


    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            nxt = curr.next      # save next node
            curr.next = prev     # reverse pointer
            prev = curr          # advance prev
            curr = nxt           # advance curr

        return prev