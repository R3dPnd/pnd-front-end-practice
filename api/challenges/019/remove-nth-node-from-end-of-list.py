# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # We need to determine the end of the list
        # We need a way to go back to the nth node
        # We must remove this node
        visited_nodes = []
        last_node = None

        curr_node = head

        while curr_node:
            visited_nodes.append(curr_node)
            curr_node = curr_node.next
    
    def removeNthFromEndSet(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # We need to determine the end of the list
        # We need a way to go back to the nth node
        # We must remove this node
        visited_nodes = []
        last_node = None

        curr_node = head

        while curr_node:
            visited_nodes.append(curr_node)
            curr_node = curr_node.next