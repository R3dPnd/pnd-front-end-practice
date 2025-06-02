# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize a dummy head node to simplify the list construction
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0
        
        # Continue while we have digits in either list or a carry
        while l1 or l2 or carry:
            # Get values from the lists, defaulting to 0 if node is None
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            
            # Calculate sum and new carry
            total = x + y + carry
            carry = total // 10
            digit = total % 10
            
            # Create new node with the calculated digit
            current.next = ListNode(digit)
            current = current.next
            
            # Move to next nodes if they exist
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        # Return the result list (skip the dummy head)
        return dummy_head.next