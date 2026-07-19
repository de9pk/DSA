import math
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        min_=min(nums)
        max_=max(nums)

        ans = gcd(min_,max_)
        return ans