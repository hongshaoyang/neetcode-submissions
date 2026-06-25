# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        return self.traverse(root, subRoot)


    def traverse(self, root, subRoot) -> bool:
        if not root:
            return False

        if root.val == subRoot.val and self.same_tree(root, subRoot):
            return True


        return self.traverse(root.left, subRoot) or self.traverse(root.right, subRoot)

        

    def same_tree(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        if (left is None and right is None):
            return True

        if (left is None and right is not None):
            return False
        if (right is None and left is not None):
            return False

        return left.val == right.val and self.same_tree(left.left, right.left) and self.same_tree(left.right, right.right)
            
