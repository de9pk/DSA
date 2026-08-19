class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l=1
        r=max(nums)

        while l<=r:
            d=(l+r)//2
            cs=0 #current sum
            for num in nums:
                cs+=(num+d-1)//d

            if cs<=threshold:
                r=d-1
            else:
                l=d+1
        
        return l
        
        


            