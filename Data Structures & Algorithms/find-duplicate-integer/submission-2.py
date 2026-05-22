class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        fast = 0
        slow = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if fast == slow:
                break
        
        slow = 0

        while True:
            slow = nums[slow]
            fast = nums[fast]
        
            if fast == slow:
                break
        
        return fast
        