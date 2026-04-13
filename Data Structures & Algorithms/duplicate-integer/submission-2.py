class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        dictionary = {}

        for num in nums:
            if num in dictionary:
                return True
            dictionary[num] = dictionary.get(num, 0) + 1
        
        return False