class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans = [1]*n

        prefix_p = 1
        for i in range(n):
            ans[i] = prefix_p
            prefix_p *= nums[i]
        
        suffix_p = 1
        for i in range(n-1,-1,-1):
            ans[i]*=suffix_p
            suffix_p *= nums[i]
        
        return ans