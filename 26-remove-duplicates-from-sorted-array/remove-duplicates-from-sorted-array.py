class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        l=0
        r=1
        ans=[]
        while r<len(nums):
            if nums[l]==nums[r]:
                r+=1
            else:
                l+=1
                nums[l]=nums[r]
                r+=1
        
        return l+1
            
            