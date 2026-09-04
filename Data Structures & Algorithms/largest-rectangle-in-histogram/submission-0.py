class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        left_bound = 0
        right_bound = 0
        max_area = 0
        
        for i, current_height in enumerate(heights):
            while stack and current_height < heights[stack[-1]]:
                right_bound = stack.pop()

                if stack:
                    left_bound = stack[-1]
                else:
                    left_bound = -1
            
                width = i - left_bound - 1
                area = heights[right_bound] * width
                max_area = max(max_area, area)

            stack.append(i)
            
        while stack:
            current_bar_index = stack.pop()

            if stack:
                left_bound = stack[-1]
            else:
                left_bound = -1
            
            width = len(heights) - left_bound - 1
            area = heights[current_bar_index] * width
            max_area = max(max_area, area)

        return max_area