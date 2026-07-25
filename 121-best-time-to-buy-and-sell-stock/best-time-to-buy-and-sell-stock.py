class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        r=l+1
        ans = 0

        while r<len(prices):
            if prices[r]>prices[l]:
                diff = prices[r]-prices[l]
                ans = max(ans,diff)
            
            else:
                l=r
        
            r+=1
            
        return ans