# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while True:
            if not slow:
                break
            if not fast or not fast.next:
                break
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False

        