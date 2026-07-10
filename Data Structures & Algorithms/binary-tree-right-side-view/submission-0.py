# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        res, q = [], deque([root])

        while len(q) > 0:
            last_val = None
            for i in range(len(q)):

                node = q.popleft()
                if node:
                    last_val = node.val
                    q.append(node.left)
                    q.append(node.right)
            if last_val:
                res.append(last_val)
        return res
        