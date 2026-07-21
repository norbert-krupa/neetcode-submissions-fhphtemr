class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        if not nums:
            return []

        result = []
        path = []

        def backtrack(start, path_sum):

            if path_sum == target:
                result.append(path[:])
            elif path_sum < target:
                for i in range(start, len(nums)):
                    path.append(nums[i])
                    backtrack(i, path_sum + nums[i])
                    path.pop()
        
        backtrack(0, 0)
        return result


        