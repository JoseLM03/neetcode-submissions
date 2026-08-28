class Solution:
    def minWindow(self, s: str, t: str) -> str:
        frequency = {}
        window = {}
        left = 0

        for char in t:
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1
        have = 0
        need = len(frequency)
        best_length = float("inf")
        result = ""

        for right, char in enumerate (s):
            if char in window:
                window[char] += 1
            else:
                window[char] = 1

            if char in frequency and window[char] == frequency[char]:
                have += 1
        
            while have == need:
                current_length = right - left + 1
                
                if current_length < best_length:
                    best_length = current_length
                    result = s[left: right + 1]
                
                window[s[left]] -= 1

                if (s[left] in frequency and window[s[left]] <           frequency[s[left]]):
                    have -= 1
                
                if window[s[left]] == 0:
                    window.pop(s[left])
                    
                left += 1
        return result



        
        
