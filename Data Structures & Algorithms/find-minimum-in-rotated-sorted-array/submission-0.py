class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        min_element = nums[0]
        left, right = 0, len(nums) - 1

        while left <= right:
            if nums[left] < nums[right]:
                min_element = min(min_element, nums[left])
                break
            
            mid = (left + right) // 2
            min_element = min(min_element, nums[mid])
            
            if nums[left] <= nums[mid]:
                left = mid + 1
            elif nums[right] > nums[mid]:
                right = mid - 1
        
        return min_element
 