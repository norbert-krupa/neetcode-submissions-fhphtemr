class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        result = []
        run_prod = 1

        for i in range(0, len(nums)):
            result.append(run_prod)
            run_prod *= nums[i]
        
        run_prod = 1

        for i in range(len(nums) - 1, -1, -1):
            result[i] *= run_prod
            run_prod *= nums[i]
            
        return result




