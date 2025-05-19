# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()

        curr = head
        while curr:
            curr = curr.next
            if curr in visited:
                return True
            else:
                visited.add(curr)
        
        return False