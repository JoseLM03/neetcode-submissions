# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head) # Dummy points to original head
        slow = dummy
        fast = dummy
        
        for _ in range(n): # Repeat exactly n times
            fast = fast.next # Move fast forward one node

        # Move both pointers until fast reaches the last node
        while fast.next:
            slow = slow.next # Move slow forward one node
            fast = fast.next

        # Skip the node that needs to be removed
        slow.next = slow.next.next 

        return dummy.next # Dummy may now point to a new head