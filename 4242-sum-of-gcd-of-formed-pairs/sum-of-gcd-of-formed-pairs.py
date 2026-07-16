import math
class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        
        ans = []
        mx=0
        for num in nums:
            mx = max(mx,num)
            curr = gcd(num,mx)
            ans.append(curr)

        ans.sort()

        total_sum = 0
        n = len(ans)
        l=0
        r=n-1

        while l<r:
            total_sum+= gcd(ans[l],ans[r])
            l+=1
            r-=1
        
        return total_sum








        

