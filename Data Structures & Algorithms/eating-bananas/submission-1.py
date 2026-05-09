class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #find the min eating banana rate k that less than or equal than h
        #k = [1....h], piles = [2,4,5,10] k = 1 mean it took piles[i]/1 hours to eat the each piles
        left = 1
        ans = right = max(piles) 

        while left <= right:
            k = (left + right) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p / k) #compute total time eating banan with k rate
            if hours <= h:
                ans = min(ans, k) #looking for the min rate k <= h
                right = k - 1
            else: 
                left = k + 1
        return ans


        