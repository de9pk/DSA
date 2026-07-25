class Solution:
    def maxProduct(self, n: int) -> int:
        ans = 1
        res = []
        while n>0:
            ans = (n%10)
            res.append(ans)
            n = n//10

        if len(res) < 2:
            return res[0]
            
        p = 0
        l=0
        r=1
        while l<len(res)-1:
            p = max(p, res[l] * res[r])
            r+=1

            if r == len(res):
                l+=1
                r=l+1

        return p