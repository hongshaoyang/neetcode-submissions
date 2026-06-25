# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        res = 0
        def dfs_height(root):
            nonlocal res

            if not root:
                return 0
            if (not root.left and not root.right):
                return 1 # leaf has height 1
            left_height = dfs_height(root.left)
            right_height = dfs_height(root.right)


            res = max(res, left_height + right_height)
            
            
            return 1 + max(left_height, right_height)


        dfs_height(root)

        return res




        