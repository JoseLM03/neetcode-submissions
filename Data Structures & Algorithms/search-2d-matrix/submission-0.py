class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        num_of_cols = len(matrix[0])
        right = len(matrix) * num_of_cols - 1
        
        while left <= right:
            mid = (left + right) // 2
            row = mid // num_of_cols
            col = mid % num_of_cols

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                left = mid + 1 # Search the right half
            elif matrix[row][col] > target:
                right = mid - 1 # Search the left half

        return False