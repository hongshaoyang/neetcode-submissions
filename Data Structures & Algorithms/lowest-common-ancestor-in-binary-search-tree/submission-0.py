# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        if p.val < q.val:
            v1, v2 = p.val, q.val
        else:
            v1, v2 = q.val, p.val


        def dfs(curr, v1, v2):
            ''' 
            v1    curr   v2
            '''
            if v1 < curr.val and curr.val < v2:
                return curr

            if curr.val < v1:
                return dfs(curr.right, v1, v2)

            if v2 < curr.val:
                return dfs(curr.left, v1, v2)
            
            if curr.val == v1 or curr.val == v2:
                return curr

        
        return dfs(root, v1, v2)

        