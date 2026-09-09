class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:
                # Left half is sorted
                if nums[left] <= target < nums[mid]:
                    # Target is inside the sorted left half
                    right = mid - 1 
                else:
                    # Target isn't in the sorted left half
                    left = mid + 1
            else:
                # Right half is sorted
                if nums[mid] < target <= nums[right]:
                    # Target is inside the sorted right half
                    left = mid + 1 
                else:
                    # Target isn't in the sorted right half
                    right = mid - 1 
            
        if left == right:
            if nums[left] == target:
                return left
            else:
                return -1
            
            




