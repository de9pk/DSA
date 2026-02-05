class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        buy = float("inf")

        for i in range(len(prices)):
           
           if prices[i] > buy :
             profit = prices[i] - buy
             maxprofit = max(maxprofit,profit)

           else: buy = prices[i]




        return maxprofit


        

    
        
    


         


        