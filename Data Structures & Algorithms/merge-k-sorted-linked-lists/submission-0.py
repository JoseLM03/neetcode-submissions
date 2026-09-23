class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # No lists means there is nothing to merge
        if not lists:
            return None

        # Keep merging until only one list remains
        while len(lists) > 1:
            merged_lists = []

            # Merge the lists two at a time
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None

                # Add the merged pair to the next round
                merged_lists.append(self.mergeTwoLists(l1, l2))

            # Use the merged lists for the next round
            lists = merged_lists

        # Only one fully merged list remains
        return lists[0]

    def mergeTwoLists(self, l1, l2):
        # Dummy node starts the merged list
        dummy = ListNode()
        current = dummy

        # Compare nodes while both lists have nodes
        while l1 and l2:
            if l1.val <= l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next

            # Move to the node we just added
            current = current.next

        # Attach whichever list still has nodes
        current.next = l1 if l1 else l2

        # Skip the dummy node
        return dummy.next