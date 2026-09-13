# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0) # Temp starting anchor
        current = dummy # Moves as we build the merged list

        while list1 and list2: 
            
            if list1.val < list2.val:
                current.next = list1 # Attach list1's node
                list1 = list1.next # Advance list1
            else:
                current.next = list2 # Attach list2's node
                list2 = list2.next # Advance list2
            
            current = current.next # Move to node we just attached
            
        if not list1:
            # list1 ended, attach remaining list2
            current.next = list2
        else:
            current.next = list1
        
        return dummy.next