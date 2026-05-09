class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        total = 0
        length = float('inf')

        l = r = 0

        if sum(nums[0:n]) < target:
            return 0

        for r in range(n):
            total += nums[r]
            
            while total >= target:
                length = min(length,r-l+1)
                total -= nums[l]
                l += 1

        return length
        