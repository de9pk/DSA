class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum1 = 0
        sum2 = 0

        for i in nums:
            sum1 += i
        n=len(nums)
        for j in range(0,n+1):
            sum2 += j

        return sum2 - sum1