class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Start both pointers at the first value
        slow = nums[0]
        fast = nums[0]

        # Find where slow and fast meet inside the cycle
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        # Start a new pointer at the beginning
        slow2 = nums[0]

        # Move both one step until they meet
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]

        # Their meeting point is the duplicate
        return slow