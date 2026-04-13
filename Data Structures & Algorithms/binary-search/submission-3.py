class Solution:
    def search(self, nums: List[int], target: int) -> int:

        if len(nums) == 1 and target in nums:
            return 0
            
        left = 0
        right = len(nums) - 1

        while left < right:

            if nums[left] == target:
                return left
            elif nums[right] == target:
                return right
            else:
                mid = (right - left) + 1 // 2

                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
        
        return -1
