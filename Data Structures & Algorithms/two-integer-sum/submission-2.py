class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen_diffs = {}

        for i, n in enumerate(nums):
            diff = target - n

            if diff in seen_diffs:
                return [seen_diffs[diff], i]
            
            seen_diffs[n] = i