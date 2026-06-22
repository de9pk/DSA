class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)-1
        l = 1
        r = max(piles)
        

        while l<=r:
            mid = (l+r)//2
            hours = 0
            for pile in piles:
                hours += (pile + mid -1)//mid

            if hours<=h:
                r = mid-1
            else:
                l = mid+1

        return l






                    




