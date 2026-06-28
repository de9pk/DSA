class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        n=len(candies)
        l=1
        r=max(candies)

        while l<=r:
            mid = (l+r)//2
            children = 0
            for candy in candies:
                children += candy // mid

            if children>=k:
                l=mid+1
            else:
                r=mid-1
        
        return l-1
            
            