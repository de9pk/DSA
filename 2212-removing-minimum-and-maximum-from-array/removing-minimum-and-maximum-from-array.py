class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 1
        i=min(nums)
        j=max(nums)
        mid = len(nums)//2
        ii=0
        ji=0
        for n in range(len(nums)):
            if nums[n] == i:
                ii=n
        for n in range(len(nums)):
            if nums[n] == j:
                ji=n
        ans1=0
        ans2=0
        ans3=0
        l=len(nums)
        # Both removed from the left
        ans1=max(ii,ji) + 1
        # Both removed from the right
        ans2=l - min(ii,ji)
        # One from left, one from right
        ans3=min(ii, ji) + 1 + l - max(ii, ji)

        return min(ans1, ans2, ans3)

