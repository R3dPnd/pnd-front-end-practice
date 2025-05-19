from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
            
        cells = [(0, 0)]  # Initialize with a list of coordinate tuples
        order = []
        while cells:
            cell = cells.pop()
            order.append(matrix[cell[0]][cell[1]])  # Fixed indexing to use proper tuple access
        
        return order