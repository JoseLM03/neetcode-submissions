"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Map each original node to is copied node
        copies = {
            None: None
        }
        current = head

        # Pass 1: Create a copy of every node
        while current: #Visit every original node even the last one
            # Create / store copied node
            copies[current] = Node(current.val)
            current = current.next

        # Pass 2: Connect the copied nodes
        current = head

        while current:
            # Copy the next relationship
            copies[current].next = copies[current.next]
            # Copy the random relationship
            copies[current].random = copies[current.random]
            current = current.next

        return copies[head]





