class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sum1 = 0
        sum2 = 0

        for i in nums:
            sum1 = i+sum1
        
        for j in range(0,n+1):
            sum2 = j+sum2

        return sum2 - sum1




        

        
               
        
 

              
            