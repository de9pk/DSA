import math
class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:

        sum1=0
        sum2=0

        for i in range(1,n):
            sum1+=(2*i-1)
        
        for i in range(1,n):
            sum2+=(2*i)

        result = math.gcd(sum1,sum2)

        return result+1

        