class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # s2 must be at least as long as s1
        if len(s1) > len(s2):
            return False
        
        # Count the characters in s1
        s1_count = {}

        for char in s1:
            if char in s1_count:
                s1_count[char] += 1
            else:
                s1_count[char] = 1
        
        # Track the current window in s2
        s2_count = {}
        left = 0
        
        for right, char in enumerate(s2):
            # Add the current character to the window
            if char in s2_count:
                s2_count[char] += 1
            else:
                s2_count[char] = 1
        
            # Shrink the window if it is too large
            if right - left + 1 > len(s1):
                s2_count[s2[left]] -= 1
                if s2_count[s2[left]] == 0:
                    s2_count.pop(s2[left])
                left += 1
        
        # Check if the current window is a permutation of s1
            if s2_count == s1_count:
                return True
        
        # No permutation was found
        return False