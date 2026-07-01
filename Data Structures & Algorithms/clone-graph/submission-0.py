"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        clone_map = {}

        def dfs(curr): # returns clone of curr
            if not curr:
                return
            if curr in clone_map: # visited
                return


            # visit
            curr2 = Node(curr.val, [])
            clone_map[curr] = curr2

            for curr_n in curr.neighbors:
                dfs(curr_n)
                curr2.neighbors.append(clone_map[curr_n])

            return curr2
            
        
        return dfs(node)
        