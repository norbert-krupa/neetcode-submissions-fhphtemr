class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen_diffs = {}

        for i, num in enumerate(nums):
            diff = target - num

            if diff in seen_diffs:
                return [seen_diffs[diff], i]
            
            seen_diffs[num] = i