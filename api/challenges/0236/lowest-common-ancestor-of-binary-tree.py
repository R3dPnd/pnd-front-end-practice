# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        #dfs to find rhe parents of either p or q
        parents = {root: None}
        stack = [root]

        while p not in parents and q not in parents:
            curr = stack.pop()

            if curr.right:
                parents[curr.right] = curr
                stack.append(curr.right)
            if curr.left:
                parents[curr.right] = curr
                stack.append(curr.left)
        
        p_parents = set()

        while p:
            p = parents[p]
            p_parents.add(p)

        while q not in p_parents:
            q = p_parents[q]
        
        return q

        
            

        