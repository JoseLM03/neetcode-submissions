# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None # Nothing comes before the original head
        current = head # Start at the first node
        while current:
            # Save the next node before breaking the link
            next_node = current.next 
            current.next = previous # Reverse the arrow
            previous = current # Move previous forward
            current = next_node # Move current forward
        
        return previous