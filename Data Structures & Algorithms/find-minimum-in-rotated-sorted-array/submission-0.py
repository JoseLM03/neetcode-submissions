class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0 # Left boundary of the part we're still searching
        # Right boundary of the part we're still searching
        right = len(nums) - 1 # Last valid index in the array
        
        while left < right:
            mid = (left + right) // 2
            
            if nums[mid] > nums[right]:
                left = mid + 1 # Minimum is to the right of mid
            else:
                right = mid # Mid could be the minimum, so keep it
        
        return nums[left] # left == right, so return the minimum value