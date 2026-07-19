import math
class Solution:
    def gcd(self,a,b):
            while b:
                a,b = b,a%b
            
            return a

    def findGCD(self, nums: List[int]) -> int:

        min_=min(nums)
        max_=max(nums)

        return self.gcd(min_,max_)