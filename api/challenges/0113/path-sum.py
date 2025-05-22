# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        def bfs(node, sum, path):  
            if node is None:
                return
            new_sum = sum + node.val     
            if node.left is None and node.right is None and new_sum == targetSum:
                path.append(node.val)
                solutions.append(path.copy())
                path.pop()
                return

            new_path = path.copy()
            new_path.append(node.val)
            bfs(node.left, new_sum, new_path)
            bfs(node.right, new_sum, new_path)
        
        solutions = []
        bfs(root, 0, [])
        return solutions