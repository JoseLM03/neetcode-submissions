from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = deque()
        result = []

        for right, num in enumerate(nums):

            while window and nums[window[-1]] < num:
                window.pop()

            window.append(right)

            if window[0] < right - k + 1:
                window.popleft()

            if right >= k - 1:
                result.append(nums[window[0]])
            
        return result