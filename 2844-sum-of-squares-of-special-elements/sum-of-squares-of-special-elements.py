class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n=len(nums)
        ans=0
        for i,j in enumerate(nums):
            if n%(i+1) ==0:
                ans +=(j*j)
        
        return ans