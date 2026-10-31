class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        #return min rate bananas per hour eating k
        #rate is piles[i] / k (round up)
        #k = [1, max of the banana in pile]
        #k = [1,2,3,4, 5] when piles = [2,1, 4, 5]
        #binary search through the hours eating banaa
        left = 1
        right = max(piles)
        res = right 

        while left <= right:
            k = (right + left) // 2
            #count how many hours it take to eat all the bananas
            hours = 0
            for i in piles:
                hours += math.ceil(i / k)
            if hours <= h:
                res = min(res, k)
                right = k - 1 #because it valid so lower right to find the minimum
            else:
                left = k + 1
        return res

