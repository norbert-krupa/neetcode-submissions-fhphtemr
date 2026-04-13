class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        k = max(piles)
        left, right = 1, k

        while left <= right:
            temp_k = (left + right) // 2
            time = 0

            for p in piles:
                time += -(-p // temp_k)
            
            if time <= h:
                k = temp_k
                right = temp_k - 1
            else:
                left = temp_k + 1
        
        return k

            







        