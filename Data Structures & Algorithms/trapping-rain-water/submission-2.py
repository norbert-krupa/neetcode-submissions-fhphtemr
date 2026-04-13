class Solution:
    def trap(self, height: List[int]) -> int:
        
        water_l = [0] * len(height)
        water_r = [0] * len(height)

        i = 0
        while i < len(height):
            if height[i] > 0:
                j = i + 1
                while j < len(height) and height[j] < height[i]:
                    water_l[j] = height[i] - height[j]
                    j += 1
                i = j
            else:
                i += 1
        
        i = len(height) - 1
        while i >= 0:
            if height[i] > 0:
                j = i - 1
                while j >= 0 and height[j] < height[i]:
                    water_r[j] = height[i] - height[j]
                    j -= 1
                i = j
            else:
                i -= 1
        
        max_water = 0

        for i in range(len(water_l)):
            max_water += min(water_l[i], water_r[i])
        
        return max_water



        
