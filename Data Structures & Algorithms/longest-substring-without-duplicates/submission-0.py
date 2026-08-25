class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        max_length = 0
        
        for char in s:
            if char in seen:
                while char in seen:
                    seen.remove(s[left])
                    left += 1

            seen.add(char)
            max_length = max(max_length, len(seen))
        
        return max_length