class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1 #Slowest possible eating rate
        right = max(piles) #Fastest rate needed to finish any pileIn1HR

        while left < right:
            k = (left + right) // 2 #Test middle eating rate
            total_hours = 0

            for pile in piles:
                total_hours += (pile + k - 1) // k # Add hrs needed

            if total_hours <= h:
                right = k #k works, search for smaller rate
            else:
                left = k + 1 #k is too slow, search faster
                
        return left
