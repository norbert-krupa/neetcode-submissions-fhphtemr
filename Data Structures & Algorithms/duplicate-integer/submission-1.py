class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        dictionary = {}

        for num in nums:
            dictionary[num] = dictionary.get(num, 0) + 1
            
        
        for _, value in dictionary.items():
            if value > 1:
                return True
        
        return False