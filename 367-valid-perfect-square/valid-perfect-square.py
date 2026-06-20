class Solution:
    def isPerfectSquare(self, nums: int) -> bool:
        l=1
        h=nums

        while l<=h:
            mid = (l+h)//2

            if mid*mid == nums:
                return True
            elif mid*mid > nums:
                h=mid-1
            else:
                l=mid+1

        return False


