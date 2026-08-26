class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        count = {}
        max_length = 0
        
        for right, char in enumerate (s):

            #count the current character
            if char in count:
                count[char] += 1
            else:
                count[char] = 1

            #check if window is invalid
            while right - left + 1 - max(count.values()) > k:
                #remove leftmost character from our window
                count[s[left]] -= 1
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length
            