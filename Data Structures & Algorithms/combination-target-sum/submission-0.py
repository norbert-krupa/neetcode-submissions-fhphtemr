class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        if not nums:
            return []

        result = []
        path = []

        def backtrack(start):

            if sum(path) == target:
                result.append(path[:])
            elif sum(path) < target:
                for i in range(start, len(nums)):
                    path.append(nums[i])
                    backtrack(i)
                    path.pop()
        
        backtrack(0)
        return result


        