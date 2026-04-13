class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        left, right = 0, len(matrix) - 1

        while left <= right:
            mid = (left + right) // 2

            if matrix[mid][0] <= target <= matrix[mid][-1]:
                left_m, right_m = 0, len(matrix[mid]) - 1

                while left_m <= right_m:
                    mid_m = (left_m + right_m) // 2

                    if matrix[mid][mid_m] > target:
                        right_m = mid_m - 1
                    elif matrix[mid][mid_m] < target:
                        left_m = mid_m + 1
                    else:
                        return True
                
                return False

            elif matrix[mid][-1] > target:
                right = mid - 1
            elif matrix[mid][0] < target:
                left = mid + 1

        return False