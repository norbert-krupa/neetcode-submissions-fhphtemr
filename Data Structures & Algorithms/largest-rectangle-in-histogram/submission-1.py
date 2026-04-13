class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        max_rect = 0

        for i in range(len(heights)):

            left = i
            right = i

            while left >= 0 and heights[left] >= heights[i]:
                left -= 1

            while right < len(heights) and heights[right] >= heights[i]:
                right += 1
            
            curr_rect = heights[i] * (right - left - 1)

            max_rect = max(max_rect, curr_rect)
        
        return max_rect


