class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        if len(nums1) > len(nums2): # nums1 is too big
            nums1, nums2 = nums2, nums1 #Swap the two arrays

        # Total amount of numbers across both arrays
        total = len(nums1) + len(nums2)
        
        # How many numbers the COMBINED left side needs.
        # If total is odd, the left side gets the extra number.
        required_left = (total+1) // 2
        
        left = 0 # Cut before every element
        right = len(nums1) # Cut after every element

        while left <= right:
            # How many nums1 contributes to the left
            cut1 = (left + right) // 2 
            
            # nums2 supplies the rest of the left side
            cut2 = required_left - cut1

            if cut1 == 0:
                nums1_left = float("-inf") # nothin exists on left
            else:
                nums1_left = nums1[cut1 - 1] # Last element b4 the cut

            if cut1 == len(nums1):
                nums1_right = float("inf") # nothin exists on right
            else:
                nums1_right = nums1[cut1] # First element after the cut
            
            if cut2 == 0:
                nums2_left = float("-inf") # nothin exists on left
            else:
                nums2_left = nums2[cut2 - 1] # Last element b4 the cut

            if cut2 == len(nums2):
                nums2_right = float("inf") # nothin exists on right
            else:
                nums2_right = nums2[cut2] # First element after the cut
            
            if nums1_left <= nums2_right and nums2_left <= nums1_right:
                if total % 2 == 1:
                    return max(nums1_left, nums2_left) 
                else:
                    return ((max(nums1_left, nums2_left)) + (min(nums1_right, nums2_right))) / 2

            elif nums1_left > nums2_right: # cut1 is too far right
                right = cut1-1
            else:
                left = cut1 + 1

