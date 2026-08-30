class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for char in s:
            if char in "({[":
                stack.append(char)
            else:
                if stack:
                    if mapping[char] == stack[-1]:
                        stack.pop()
                    else:
                        return False
                else:
                    return False

        if not stack:
            return True
        else:
            return False