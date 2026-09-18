class Solution:
    def addTwoNumbers(self,l1: Optional[ListNode],l2: Optional[ListNode]) -> Optional[ListNode]:
        # Temporary starter node
        dummy=ListNode(0)
        # Tracks the end of the result list
        current=dummy
        # Carry from the previous addition
        carry=0

        while l1 or l2:
            # Use l1's digit, or 0 if l1 is empty
            value1=l1.val if l1 else 0
            # Use l2's digit, or 0 if l2 is empty
            value2=l2.val if l2 else 0

            # Add both digits and the carry
            total=value1+value2+carry
            # Ones digit goes into the result
            digit=total%10
            # Tens digit becomes the new carry
            carry=total//10

            # Add the new digit to the result
            current.next=ListNode(digit)
            # Move current to the new end
            current=current.next

            # Move l1 forward if it still exists
            if l1:
                l1=l1.next

            # Move l2 forward if it still exists
            if l2:
                l2=l2.next

        # Add a final carry if one remains
        if carry:
            current.next=ListNode(carry)

        # Skip the dummy node
        return dummy.next