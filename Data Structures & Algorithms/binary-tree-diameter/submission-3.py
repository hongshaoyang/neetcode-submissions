# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        if (not root.left and not root.right):
            return 0 

        l_h = self.max_height(root.left)
        r_h = self.max_height(root.right)
        curr_diameter = l_h + r_h


        l_d = self.diameterOfBinaryTree(root.left)
        r_d = self.diameterOfBinaryTree(root.right)

        return max(curr_diameter, l_d, r_d)


    def max_height(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return (
            1 + # for root
            max(self.max_height(root.left), self.max_height(root.right))
        ) 
          