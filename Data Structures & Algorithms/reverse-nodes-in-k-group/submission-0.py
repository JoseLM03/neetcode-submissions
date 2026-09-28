class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Dummy node keeps access to the head
        dummy = ListNode(0, head)
        group_prev = dummy

        while True:
            # Find the kth node of the current group
            kth = group_prev

            for _ in range(k):
                kth = kth.next

                # Fewer than k nodes remain
                if not kth:
                    return dummy.next

            # Save the node after this group
            group_next = kth.next

            # Reverse the current group
            prev = group_next
            current = group_prev.next

            while current != group_next:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node

            # Save the old start, which is now the end
            old_group_start = group_prev.next

            # Connect the previous part to the reversed group
            group_prev.next = kth

            # Move group_prev to the end of this group
            group_prev = old_group_start