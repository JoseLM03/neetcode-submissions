# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Phase 1: Find the middle of the linked list
        slow = head # Moves one node at a time
        fast = head # Moves two nodes at a time

        while fast and fast.next: #Makes sure fast can move 2 steps
            slow = slow.next # Move forward 1 node
            fast = fast.next.next # Move forward 2 nodes
        
        # Phase 2: Split and reverse the second half
        current = slow.next # Start at the 1st node of the 2nd half
        previous = None # Nothing precedes it in the reversed half yet
        slow.next = None # Cut the 1st half away from the 2nd half
        
        while current:
            # Save the next node before chaing current.next
            next_node = current.next
            current.next = previous # FLIP the arrow backward
            # Move previous onto node we just received
            previous = current
            # Move current to the original next node
            current = next_node
        
        first = head # Start of first half
        second = previous # Start of reversed second half
        
        while second:
            temp1 = first.next # Save the next node in the first half
            temp2 = second.next # Save the next node in the 2nd half
            
            # Weave 2nd-half node after 1st-half node
            first.next = second
            second.next = temp1 # Reconnect to the first half
            
            first = temp1 # Advance first
            second = temp2 # Advance second




